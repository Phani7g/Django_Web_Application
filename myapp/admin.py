from django.contrib import admin
from .models import Topic, Course, Student, Order, Review
from django.db.models.functions import Lower


# changing admin view in admin portal
class CourseInline(admin.TabularInline):
    model = Course


def reduce_price(modeladmin, request, queryset):
    for obj in queryset:
        obj.price = obj.price - ((10 * obj.price) / 100)
        obj.save()


def increase_price(modeladmin, request, queryset):
    for obj in queryset:
        obj.price = obj.price + ((10 * obj.price) / 100)
        obj.save()


class CourseAdmin(admin.ModelAdmin):
    fields = [('title', 'topic'), ('price', 'num_reviews', 'for_everyone')]
    list_display = ('title', 'topic', 'price')
    actions = [reduce_price, increase_price]


class OrderAdmin(admin.ModelAdmin):
    fields = ['courses', ('student', 'order_status', 'order_date')]
    list_display = ('id', 'student', 'order_status', 'order_date', 'total_items')


class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'length')
    inlines = [CourseInline,
               ]

    #def get_ordering(self, request):
     #   return [Lower('length')]


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'level')
    fields = [('first_name', 'last_name'), ('registered_courses', 'interested_in')]


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'course', 'rating')
    fields = ['reviewer', ('course', 'rating', 'date'), 'comments']


# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review, ReviewAdmin)
