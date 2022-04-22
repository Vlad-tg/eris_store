from .models import Product, VideoLaptop, OperatingSystemLaptop, RAM, CPULaptop, Category
from django.db.models import Q
from django.shortcuts import render
from .views import View, DetailView
from .mixins import CartMixin, AccountMixins


class FilterLaptopView(AccountMixins, CartMixin, View):

    def get(self, request, *args, **kwargs):

        qs = Product.objects.filter(category_id=1)
        products_laptop = Product.objects.all()
        videos = VideoLaptop.objects.all().order_by('-name')
        operating_systems = OperatingSystemLaptop.objects.all()
        rams = RAM.objects.all()
        processors = CPULaptop.objects.all().order_by('-name')
        screen_sizes = Product.objects.filter(category_id=1).values("screen_size").distinct()
        resolutions = Product.objects.filter(category_id=1).values("resolution").distinct()
        storage_drive_sizes = Product.objects.filter(category_id=1).values("storage_drive_size").distinct()
        video = request.GET.getlist("video")
        operating_system = request.GET.getlist("operating_system")
        ram = request.GET.getlist("ram")
        storage_drive_size = request.GET.getlist("storage_drive_size")
        processor = request.GET.getlist("processor")
        screen_size = request.GET.getlist("screen_size")
        resolution = request.GET.getlist("resolution")

        if qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )

    #  -------------------------------------------------------------------   7

    #  -------------------------------------------------------------------   6
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )

            if not processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not resolution or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or processor:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not processor or storage_drive_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or ram:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or video:
                qs = Product.objects.none()

            # ------------------------------------------------------------------------------  6

            # ----------------------------------------------------------------------------  5

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not video or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not processor or storage_drive_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not video or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not ram or operating_system or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not operating_system or video or resolution:
                qs = Product.objects.none()

            # ------------------ Resolution 5--------------------- #

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not resolution or storage_drive_size or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not video or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not ram or operating_system or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not operating_system or video or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or video or processor:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or video or storage_drive_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or video or ram:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not ram or video or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not video or storage_drive_size or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not video or ram or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not operating_system or storage_drive_size or ram:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(operating_system__id__in=operating_system) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not operating_system or storage_drive_size or processor:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(operating_system__id__in=operating_system) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or ram or processor:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(ram__id__in=ram) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or operating_system or processor:
                qs = Product.objects.none()

            #  --------------------------------------------------------------------  5

            #  ------------------------------------------------------------------   4

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size)
            )
            if not video or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor)
            )
            if not processor or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not operating_system or ram or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not ram or operating_system or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not operating_system or video or screen_size or resolution:
                qs = Product.objects.none()

            # ------------------  Screen_size  4--------------------- #

        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not processor or video or operating_system or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or video or processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or operating_system or processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(processor__id__in=processor) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not video or operating_system or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or processor or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not processor or storage_drive_size or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or storage_drive_size or video or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(graphics__id__in=video) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or storage_drive_size or operating_system or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not operating_system or video or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size)
            )
            if not ram or processor or storage_drive_size or resolution:
                qs = Product.objects.none()

            # ------------------ Resolution 4--------------------- #

        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not processor or video or operating_system or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or video or processor or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or operating_system or processor or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(processor__id__in=processor) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not video or operating_system or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or processor or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not processor or storage_drive_size or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not ram or storage_drive_size or video or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(graphics__id__in=video) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not resolution or storage_drive_size or operating_system or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not operating_system or video or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(resolution__in=resolution)
            )
            if not ram or processor or storage_drive_size or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not video or processor or storage_drive_size or ram:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or processor or storage_drive_size or video:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or processor or storage_drive_size or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not storage_drive_size or processor or video or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not processor or storage_drive_size or video or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not storage_drive_size or processor or ram or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not processor or storage_drive_size or ram or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not operating_system or storage_drive_size or ram or video:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or operating_system or ram or video:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(operating_system__id__in=operating_system) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not operating_system or processor or ram or video:
                qs = Product.objects.none()

            # -----------------------------------------------------------------    4

            #  ----------------------------------------------------------------    3

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram)
            )
            if not video or storage_drive_size or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size)
            )
            if not storage_drive_size or ram or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size)
            )
            if not storage_drive_size or video or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(graphics__id__in=video) &
                Q(storage_drive_size__in=storage_drive_size)
            )
            if not video or operating_system or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(graphics__id__in=video) &
                Q(processor__id__in=processor)
            )
            if not video or operating_system or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor)
            )
            if not operating_system or video or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor)
            )
            if not video or ram or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not storage_drive_size or operating_system or video or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not video or operating_system or ram or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not processor or video or ram or screen_size or resolution:
                qs = Product.objects.none()

            # ------------------  Screen_size  3--------------------- #

        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or video or ram or processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not video or ram or processor or operating_system or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not ram or processor or operating_system or video or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or operating_system or video or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or operating_system or storage_drive_size or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size)
            )
            if not video or processor or storage_drive_size or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size)
            )
            if not ram or processor or storage_drive_size or operating_system or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or video or storage_drive_size or operating_system or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not operating_system or video or storage_drive_size or ram or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or video or storage_drive_size or processor or resolution:
                qs = Product.objects.none()

            # ------------------ Resolution 3--------------------- #
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not operating_system or video or ram or processor or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not video or ram or processor or operating_system or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not ram or processor or operating_system or video or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not storage_drive_size or operating_system or video or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(graphics__id__in=video) &
                Q(resolution__in=resolution)
            )
            if not resolution or operating_system or storage_drive_size or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(graphics__id__in=video) &
                Q(resolution__in=resolution)
            )
            if not resolution or processor or storage_drive_size or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(graphics__id__in=video) &
                Q(resolution__in=resolution)
            )
            if not ram or processor or storage_drive_size or operating_system or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not processor or video or storage_drive_size or operating_system or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not operating_system or video or storage_drive_size or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram) &
                Q(resolution__in=resolution)
            )
            if not resolution or video or storage_drive_size or processor or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or video or storage_drive_size or processor or ram:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or video or storage_drive_size or processor or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not processor or video or storage_drive_size or ram or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or processor or storage_drive_size or ram or operating_system:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not storage_drive_size or processor or video or ram or operating_system:
                qs = Product.objects.none()

            # ------------------------------------------------------------------   3

            # ------------------------------------------------------------------    2

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(operating_system__id__in=operating_system)
            )
            if not video or ram or processor or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(ram__id__in=ram)
            )
            if not ram or operating_system or processor or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(ram__id__in=ram)
            )
            if not ram or storage_drive_size or video or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(storage_drive_size__in=storage_drive_size)
            )
            if not operating_system or ram or video or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(storage_drive_size__in=storage_drive_size)
            )
            if not video or operating_system or ram or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(storage_drive_size__in=storage_drive_size)
            )
            if not ram or video or operating_system or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(processor__id__in=processor)
            )
            if not processor or operating_system or video or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(processor__id__in=processor)
            )
            if not storage_drive_size or video or ram or operating_system or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(processor__id__in=processor)
            )
            if not operating_system or ram or video or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(processor__id__in=processor)
            )
            if not video or operating_system or ram or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()

            # ------------------ Screen_size 2--------------------- #

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or operating_system or ram or storage_drive_size or processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(screen_size__in=screen_size)
            )
            if not processor or operating_system or ram or storage_drive_size or video or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or ram or storage_drive_size or video or processor or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(screen_size__in=screen_size)
            )
            if not ram or storage_drive_size or video or processor or operating_system or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(screen_size__in=screen_size)
            )
            if not screen_size or video or processor or operating_system or ram or resolution:
                qs = Product.objects.none()

            # ------------------ Resolution 2--------------------- #

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video) &
                Q(resolution__in=resolution)
            )
            if not resolution or operating_system or ram or storage_drive_size or processor or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor) &
                Q(resolution__in=resolution)
            )
            if not processor or operating_system or ram or storage_drive_size or video or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system) &
                Q(resolution__in=resolution)
            )
            if not operating_system or ram or storage_drive_size or video or processor or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram) &
                Q(resolution__in=resolution)
            )
            if not ram or storage_drive_size or video or processor or operating_system or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size) &
                Q(resolution__in=resolution)
            )
            if not resolution or video or processor or operating_system or ram or screen_size:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(screen_size__in=screen_size) &
                Q(resolution__in=resolution)
            )
            if not screen_size or video or processor or operating_system or ram or storage_drive_size:
                qs = Product.objects.none()

            # --------------------------------------------------------------------------    2

            # --------------------------------------------------------------------------     1

        if not qs:
            qs = Product.objects.filter(
                Q(graphics__id__in=video))
            if not video or operating_system or ram or storage_drive_size or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(operating_system__id__in=operating_system))
            if not operating_system or video or ram or storage_drive_size or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(ram__id__in=ram))
            if not ram or operating_system or video or storage_drive_size or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(storage_drive_size__in=storage_drive_size))
            if not storage_drive_size or ram or operating_system or video or processor or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(processor__id__in=processor))
            if not processor or ram or operating_system or video or storage_drive_size or screen_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(screen_size__in=screen_size))
            if not screen_size or processor or ram or operating_system or video or storage_drive_size or resolution:
                qs = Product.objects.none()
        if not qs:
            qs = Product.objects.filter(
                Q(resolution__in=resolution))
            if not resolution or processor or ram or operating_system or video or storage_drive_size or screen_size:
                qs = Product.objects.none()

            #  ------------------------------------------------------------------   1

        context = {
            'queryset': qs,
            'videos': videos,
            'operating_systems': operating_systems,
            'rams': rams,
            'screen_sizes': screen_sizes,
            'resolutions': resolutions,
            'storage_drive_sizes': storage_drive_sizes,
            'processors': processors,
            'products_laptop':  products_laptop,
            'user_id_html': self.user_id,
            'cart': self.cart,

        }

        return render(request, 'main/filter_laptop.html', context)


