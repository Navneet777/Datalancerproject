from django.contrib import admin
from info.models import Contactus , BasicInfo , Marks ,TrandingCourse , WebCourse , Trainingmodel,Post
# Register your models here.

class ContactusAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']

    model = Contactus
    field = '__all__'

class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','roll_no']

    model = BasicInfo
    field = '__all__'

class MarksAdmin(admin.ModelAdmin):
    list_display = ['name','address','english_marks','science_marks','math_marks']

    model = Marks
    field = '__all__'

class TraningmodelAdmin(admin.ModelAdmin):
    list_display = ['name' , 'course', 'phone', 'city']

    model = Trainingmodel
    field ='__all__'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Contactus,ContactusAdmin)
admin.site.register(BasicInfo,BasicInfoAdmin)
admin.site.register(Marks,MarksAdmin)
admin.site.register(TrandingCourse)
admin.site.register(WebCourse)
admin.site.register(Trainingmodel,TraningmodelAdmin)
admin.site.register(Post,PostAdmin)
