from django import forms
from . import db

class ProductForm(forms.Form):
    code = forms.CharField(max_length=30, label='Mã')
    name = forms.CharField(max_length=100, label='Tên')
    description = forms.CharField(max_length=500, required=False, label='Mô tả')
    price = forms.IntegerField(label='Giá')

    def clean_code(self):
        code = self.cleaned_data.get('code')
        id = self.initial.get('id')
        p = db.getProductByCode(code)
        
        if p != None and p['id'] != id:
            print(id, p)
            raise forms.ValidationError('Mã sản phẩm đã tồn tại')
        
        return code
