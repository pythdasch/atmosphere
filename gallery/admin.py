# -*- coding: utf-8 -*-
from django.contrib import admin
from multiupload.admin import MultiUploadAdmin
from sorl.thumbnail.admin import AdminImageMixin
from models import Image, Gallery
from django.shortcuts import get_object_or_404


class ImageAdmin(AdminImageMixin, MultiUploadAdmin):
    list_display = ('name', 'image')

    # default value of all parameters:
    change_form_template = 'multiupload/change_form.html'
    change_list_template = 'multiupload/change_list.html'
    multiupload_template = 'multiupload/upload.html'
    # if true, enable multiupload on list screen
    # generaly used when the model is the uploaded element
    multiupload_list = True
    # if true enable multiupload on edit screen
    # generaly used when the model is a container for uploaded files
    # eg: gallery
    # can upload files direct inside a gallery.
    multiupload_form = True
    # max allowed filesize for uploads in bytes
    # 3 MbPhotoGallery
    multiupload_maxfilesize = 3 * 2 ** 20
    # min allowed filesize for uploads in bytes
    multiupload_minfilesize = 0
    # tuple with mimetype accepted
    multiupload_acceptedformats = (
        "image/jpeg",
        "image/pjpeg",
        "image/png",
    )

    def process_uploaded_file(self, uploaded, object, request):

        # example:
        title = request.POST.get('title', '') or uploaded.name

        f = Image(image=uploaded, nome=title)
        f.save()
        return {
            'url': f.imagem(),
            'thumbnail_url': f.imagem(),
            'id': f.id,
            'name': f.name,
        }

    def delete_file(self, pk, request):
        '''
        Function to delete a file.
        '''
        # This is the default implementation.
        obj = get_object_or_404(self.queryset(request), pk=pk)
        obj.delete()

admin.site.register(Image, ImageAdmin)


class PhotoGallery(admin.StackedInline):
    model = Image
    extra = 0


class GalleryAdmin(admin.ModelAdmin):
    model = Gallery


admin.site.register(Gallery, GalleryAdmin)
