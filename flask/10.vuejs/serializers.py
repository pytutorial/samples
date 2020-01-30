import dataclasses
from models import Student
from sqlalchemy import inspect

class Serializer:
    class Meta:
        model = None
        schema = None
    
    def __init__(self, json, instance=None, partial=False):
        if partial and instance:
            self.data = dataclasses.asdict(instance)
            self.data.update(json)
        else:
            self.data = json
            
        self.data["id"] = instance.id if instance else None

        self.errors = []
    
    def is_valid(self):
        mapper = inspect(Student)
        for column in mapper.attrs:
            column_name = column.key
            if column_name == "id":
                continue

            column_val = self.data.get(column_name)
            unique = column.expression.unique
            nullable = column.expression.nullable
            type = column.expression.type.python_type
            maxlength = column.expression.type.length if hasattr(column.expression.type, 'length') else None
            constraint = column.expression.dialect_options.get("constraint", {})
            not_blank = constraint.get("not_blank")
            
            if unique:                
                records = self.Meta.model.query \
                                .filter(self.Meta.model.id != self.data.get("id")) \
                                .filter_by(**{column_name: column_val})

                if records.count() > 0:
                    self.errors.append({
                        "path": column.key, 
                        "message": f"Duplicated {column_name} : {column_val}"
                    })

            if not nullable and column_val == None:                
                self.errors.append({
                    "path": column.key, 
                    "message": f'This field is required'
                })

            if not_blank and not column_val or column_val.strip() == '':
                self.errors.append({
                    "path": column.key, 
                    "message": f'Value cannot be blank'
                })

            if type == str and maxlength != None and column_val != None and len(column_val) > maxlength:
                self.errors.append({
                    "path": column.key, 
                    "message": f'Value is too long, max length allowed : {maxlength}'
                })

            if type == int:
                try:
                    int(column_val)
                except:
                    self.errors.append({
                        "path": column.key, 
                        "message": f'Invalid integer value'
                    })

            if type == float:
                try:
                    float(column_val)
                except:
                    self.errors.append({
                        "path": column.key, 
                        "message": f'Invalid float value'
                    })

            if hasattr(self, "clean_" + column_name):
                method = getattr(self, "clean_" + column_name)
                try:
                    self.data[column_name] = method()
                except Exception as e:
                    self.errors.append({
                        "path": column.key, 
                        "message": str(e)
                    })
                
        return len(self.errors) == 0

    def get_object_model(self):
        if self.Meta.model:
            data = {f.name : self.data.get(f.name) for f in dataclasses.fields(self.Meta.model)}
            return self.Meta.model(**data)

class StudentSerializer(Serializer):
    class Meta:
        model = Student
    
    def clean_studentNo(self):
        studentNo = self.data.get("studentNo", '')

        if studentNo.strip() !=  '' and not studentNo.isdigit():
            raise Exception("Value must be digit")

        return studentNo
        