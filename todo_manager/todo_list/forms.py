from django import forms

from todo_list.models import ToDoItem


class ToDoCreateItemForm(forms.ModelForm):

    class Meta:
        model = ToDoItem
        fields = ('title', 'description')

        widgets = {
            'title': forms.Textarea(attrs={'cols': 20, 'rows': 5}),
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }

class ToDoItemUpdateForm(forms.ModelForm):
    class Meta(ToDoCreateItemForm.Meta):
        fields = ('title', 'description', 'done')



