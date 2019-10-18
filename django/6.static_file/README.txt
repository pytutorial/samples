Add the following lines to the end of "mysite/settings.py":
	
  STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
  ]