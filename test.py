# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminToolsDashboardPreferences(models.Model):
    data = models.TextField()
    dashboard_id = models.CharField(max_length=100)
    user = models.ForeignKey('LoginMyuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_tools_dashboard_preferences'
        unique_together = (('user', 'dashboard_id'),)


class AdminToolsMenuBookmark(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user = models.ForeignKey('LoginMyuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admin_tools_menu_bookmark'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class Bootstrap4AlertsBootstrap4Alerts(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    alert_context = models.CharField(max_length=255)
    alert_dismissable = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_alerts_bootstrap4alerts'


class Bootstrap4BadgeBootstrap4Badge(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    badge_text = models.CharField(max_length=255)
    badge_context = models.CharField(max_length=255)
    badge_pills = models.BooleanField()
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_badge_bootstrap4badge'


class Bootstrap4CardBootstrap4Card(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    card_type = models.CharField(max_length=255)
    card_context = models.CharField(max_length=255)
    card_alignment = models.CharField(max_length=255)
    card_outline = models.BooleanField()
    card_text_color = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_card_bootstrap4card'


class Bootstrap4CardBootstrap4Cardinner(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    inner_type = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_card_bootstrap4cardinner'


class Bootstrap4CarouselBootstrap4Carousel(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    template = models.CharField(max_length=255)
    carousel_interval = models.IntegerField()
    carousel_controls = models.BooleanField()
    carousel_indicators = models.BooleanField()
    carousel_keyboard = models.BooleanField()
    carousel_pause = models.CharField(max_length=255)
    carousel_ride = models.CharField(max_length=255)
    carousel_wrap = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()
    carousel_aspect_ratio = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'bootstrap4_carousel_bootstrap4carousel'


class Bootstrap4CarouselBootstrap4Carouselslide(models.Model):
    template = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    anchor = models.CharField(max_length=255)
    mailto = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    attributes = models.TextField()
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    carousel_content = models.TextField()
    tag_type = models.CharField(max_length=255)
    carousel_image = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    internal_link = models.ForeignKey('CmsPage', models.DO_NOTHING, blank=True, null=True)
    file_link = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)
    external_link = models.CharField(max_length=2040)

    class Meta:
        managed = False
        db_table = 'bootstrap4_carousel_bootstrap4carouselslide'


class Bootstrap4CollapseBootstrap4Collapse(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    siblings = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_collapse_bootstrap4collapse'


class Bootstrap4CollapseBootstrap4Collapsecontainer(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    identifier = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_collapse_bootstrap4collapsecontainer'


class Bootstrap4CollapseBootstrap4Collapsetrigger(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    identifier = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_collapse_bootstrap4collapsetrigger'


class Bootstrap4ContentBootstrap4Blockquote(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    quote_content = models.TextField()
    quote_origin = models.TextField()
    quote_alignment = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_content_bootstrap4blockquote'


class Bootstrap4ContentBootstrap4Code(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    code_content = models.TextField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_content_bootstrap4code'


class Bootstrap4ContentBootstrap4Figure(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    figure_caption = models.CharField(max_length=255)
    figure_alignment = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_content_bootstrap4figure'


class Bootstrap4GridBootstrap4Gridcolumn(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    column_type = models.CharField(max_length=255)
    column_alignment = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()
    xs_col = models.IntegerField(blank=True, null=True)
    xs_order = models.IntegerField(blank=True, null=True)
    xs_ml = models.BooleanField()
    xs_mr = models.BooleanField()
    sm_col = models.IntegerField(blank=True, null=True)
    sm_order = models.IntegerField(blank=True, null=True)
    sm_ml = models.BooleanField()
    sm_mr = models.BooleanField()
    md_col = models.IntegerField(blank=True, null=True)
    md_order = models.IntegerField(blank=True, null=True)
    md_ml = models.BooleanField()
    md_mr = models.BooleanField()
    lg_col = models.IntegerField(blank=True, null=True)
    lg_order = models.IntegerField(blank=True, null=True)
    lg_ml = models.BooleanField()
    lg_mr = models.BooleanField()
    xl_col = models.IntegerField(blank=True, null=True)
    xl_order = models.IntegerField(blank=True, null=True)
    xl_ml = models.BooleanField()
    xl_mr = models.BooleanField()
    lg_offset = models.IntegerField(blank=True, null=True)
    md_offset = models.IntegerField(blank=True, null=True)
    sm_offset = models.IntegerField(blank=True, null=True)
    xl_offset = models.IntegerField(blank=True, null=True)
    xs_offset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bootstrap4_grid_bootstrap4gridcolumn'


class Bootstrap4GridBootstrap4Gridcontainer(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    container_type = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_grid_bootstrap4gridcontainer'


class Bootstrap4GridBootstrap4Gridrow(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    vertical_alignment = models.CharField(max_length=255)
    horizontal_alignment = models.CharField(max_length=255)
    gutters = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_grid_bootstrap4gridrow'


class Bootstrap4JumbotronBootstrap4Jumbotron(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    fluid = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_jumbotron_bootstrap4jumbotron'


class Bootstrap4LinkBootstrap4Link(models.Model):
    template = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    anchor = models.CharField(max_length=255)
    mailto = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    attributes = models.TextField()
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    link_type = models.CharField(max_length=255)
    link_context = models.CharField(max_length=255)
    link_size = models.CharField(max_length=255)
    link_outline = models.BooleanField()
    link_block = models.BooleanField()
    internal_link = models.ForeignKey('CmsPage', models.DO_NOTHING, blank=True, null=True)
    icon_left = models.CharField(max_length=255)
    icon_right = models.CharField(max_length=255)
    file_link = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)
    external_link = models.CharField(max_length=2040)

    class Meta:
        managed = False
        db_table = 'bootstrap4_link_bootstrap4link'


class Bootstrap4ListgroupBootstrap4Listgroup(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    list_group_flush = models.BooleanField()
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_listgroup_bootstrap4listgroup'


class Bootstrap4ListgroupBootstrap4Listgroupitem(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    list_context = models.CharField(max_length=255)
    list_state = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_listgroup_bootstrap4listgroupitem'


class Bootstrap4MediaBootstrap4Media(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_media_bootstrap4media'


class Bootstrap4MediaBootstrap4Mediabody(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_media_bootstrap4mediabody'


class Bootstrap4PictureBootstrap4Picture(models.Model):
    template = models.CharField(max_length=255)
    external_picture = models.CharField(max_length=255, blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    alignment = models.CharField(max_length=255)
    caption_text = models.TextField(blank=True, null=True)
    attributes = models.TextField()
    link_target = models.CharField(max_length=255)
    link_attributes = models.TextField()
    use_automatic_scaling = models.BooleanField()
    use_no_cropping = models.BooleanField()
    use_crop = models.BooleanField()
    use_upscale = models.BooleanField()
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    picture_fluid = models.BooleanField()
    picture_rounded = models.BooleanField()
    picture_thumbnail = models.BooleanField()
    link_page = models.ForeignKey('CmsPage', models.DO_NOTHING, blank=True, null=True)
    picture = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    thumbnail_options = models.ForeignKey('FilerThumbnailoption', models.DO_NOTHING, blank=True, null=True)
    use_responsive_image = models.CharField(max_length=7)
    link_url = models.CharField(max_length=2040, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bootstrap4_picture_bootstrap4picture'


class Bootstrap4TabsBootstrap4Tab(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    template = models.CharField(max_length=255)
    tab_type = models.CharField(max_length=255)
    tab_alignment = models.CharField(max_length=255)
    tab_index = models.PositiveIntegerField(blank=True, null=True)
    tab_effect = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_tabs_bootstrap4tab'


class Bootstrap4TabsBootstrap4Tabitem(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    tab_title = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_tabs_bootstrap4tabitem'


class Bootstrap4UtilitiesBootstrap4Spacing(models.Model):
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)
    space_property = models.CharField(max_length=255)
    space_sides = models.CharField(max_length=255)
    space_size = models.CharField(max_length=255)
    space_device = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'bootstrap4_utilities_bootstrap4spacing'


class CmsAliaspluginmodel(models.Model):
    plugin = models.ForeignKey('CmsCmsplugin', models.DO_NOTHING, blank=True, null=True)
    alias_placeholder = models.ForeignKey('CmsPlaceholder', models.DO_NOTHING, blank=True, null=True)
    cmsplugin_ptr = models.OneToOneField('CmsCmsplugin', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cms_aliaspluginmodel'


class CmsCmsplugin(models.Model):
    language = models.CharField(max_length=15)
    plugin_type = models.CharField(max_length=50)
    creation_date = models.DateTimeField()
    changed_date = models.DateTimeField()
    placeholder = models.ForeignKey('CmsPlaceholder', models.DO_NOTHING, blank=True, null=True)
    depth = models.PositiveIntegerField()
    numchild = models.PositiveIntegerField()
    path = models.CharField(unique=True, max_length=255)
    position = models.PositiveSmallIntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_cmsplugin'


class CmsGlobalpagepermission(models.Model):
    can_change = models.BooleanField()
    can_add = models.BooleanField()
    can_delete = models.BooleanField()
    can_change_advanced_settings = models.BooleanField()
    can_publish = models.BooleanField()
    can_change_permissions = models.BooleanField()
    can_move_page = models.BooleanField()
    can_view = models.BooleanField()
    can_recover_page = models.BooleanField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('LoginMyuser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission'


class CmsGlobalpagepermissionSites(models.Model):
    globalpagepermission = models.ForeignKey(CmsGlobalpagepermission, models.DO_NOTHING)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_globalpagepermission_sites'
        unique_together = (('globalpagepermission', 'site'),)


class CmsPage(models.Model):
    created_by = models.CharField(max_length=255)
    changed_by = models.CharField(max_length=255)
    creation_date = models.DateTimeField()
    changed_date = models.DateTimeField()
    publication_date = models.DateTimeField(blank=True, null=True)
    publication_end_date = models.DateTimeField(blank=True, null=True)
    in_navigation = models.BooleanField()
    soft_root = models.BooleanField()
    reverse_id = models.CharField(max_length=40, blank=True, null=True)
    navigation_extenders = models.CharField(max_length=80, blank=True, null=True)
    template = models.CharField(max_length=100)
    login_required = models.BooleanField()
    limit_visibility_in_menu = models.SmallIntegerField(blank=True, null=True)
    is_home = models.BooleanField()
    application_urls = models.CharField(max_length=200, blank=True, null=True)
    application_namespace = models.CharField(max_length=200, blank=True, null=True)
    publisher_is_draft = models.BooleanField()
    languages = models.CharField(max_length=255, blank=True, null=True)
    xframe_options = models.IntegerField()
    is_page_type = models.BooleanField()
    node = models.ForeignKey('CmsTreenode', models.DO_NOTHING)
    publisher_public = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_page'
        unique_together = (('node', 'publisher_is_draft'),)


class CmsPagePlaceholders(models.Model):
    page = models.ForeignKey(CmsPage, models.DO_NOTHING)
    placeholder = models.ForeignKey('CmsPlaceholder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_page_placeholders'
        unique_together = (('page', 'placeholder'),)


class CmsPagepermission(models.Model):
    can_change = models.BooleanField()
    can_add = models.BooleanField()
    can_delete = models.BooleanField()
    can_change_advanced_settings = models.BooleanField()
    can_publish = models.BooleanField()
    can_change_permissions = models.BooleanField()
    can_move_page = models.BooleanField()
    can_view = models.BooleanField()
    grant_on = models.IntegerField()
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(CmsPage, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('LoginMyuser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_pagepermission'


class CmsPageuser(models.Model):
    myuser_ptr = models.OneToOneField('LoginMyuser', models.DO_NOTHING, primary_key=True)
    created_by = models.ForeignKey('LoginMyuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_pageuser'


class CmsPageusergroup(models.Model):
    group_ptr = models.OneToOneField(AuthGroup, models.DO_NOTHING, primary_key=True)
    created_by = models.ForeignKey('LoginMyuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_pageusergroup'


class CmsPlaceholder(models.Model):
    default_width = models.PositiveSmallIntegerField(blank=True, null=True)
    slot = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cms_placeholder'


class CmsPlaceholderreference(models.Model):
    name = models.CharField(max_length=255)
    placeholder_ref = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'cms_placeholderreference'


class CmsStaticplaceholder(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    dirty = models.BooleanField()
    creation_method = models.CharField(max_length=20)
    draft = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    public = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_staticplaceholder'
        unique_together = (('code', 'site'),)


class CmsTitle(models.Model):
    language = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    page_title = models.CharField(max_length=255, blank=True, null=True)
    menu_title = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    has_url_overwrite = models.BooleanField()
    redirect = models.CharField(max_length=2048, blank=True, null=True)
    creation_date = models.DateTimeField()
    published = models.BooleanField()
    publisher_is_draft = models.BooleanField()
    publisher_state = models.SmallIntegerField()
    page = models.ForeignKey(CmsPage, models.DO_NOTHING)
    meta_description = models.TextField(blank=True, null=True)
    publisher_public = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cms_title'
        unique_together = (('language', 'page'),)


class CmsTreenode(models.Model):
    path = models.CharField(unique=True, max_length=255)
    depth = models.PositiveIntegerField()
    numchild = models.PositiveIntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    site = models.ForeignKey('DjangoSite', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_treenode'


class CmsUrlconfrevision(models.Model):
    revision = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cms_urlconfrevision'


class CmsUsersettings(models.Model):
    language = models.CharField(max_length=10)
    clipboard = models.ForeignKey(CmsPlaceholder, models.DO_NOTHING, blank=True, null=True)
    user = models.OneToOneField('LoginMyuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cms_usersettings'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('LoginMyuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    name = models.CharField(max_length=50)
    domain = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'django_site'


class DjangocmsFileFile(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    file_src = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)
    attributes = models.TextField()
    template = models.CharField(max_length=255)
    link_target = models.CharField(max_length=255)
    link_title = models.CharField(max_length=255)
    show_file_size = models.BooleanField()
    file_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_file_file'


class DjangocmsFileFolder(models.Model):
    template = models.CharField(max_length=255)
    link_target = models.CharField(max_length=255)
    show_file_size = models.BooleanField()
    attributes = models.TextField()
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    folder_src = models.ForeignKey('FilerFolder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_file_folder'


class DjangocmsGooglemapGooglemap(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    zoom = models.PositiveSmallIntegerField()
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    width = models.CharField(max_length=6)
    height = models.CharField(max_length=6)
    scrollwheel = models.BooleanField()
    double_click_zoom = models.BooleanField()
    draggable = models.BooleanField()
    keyboard_shortcuts = models.BooleanField()
    pan_control = models.BooleanField()
    zoom_control = models.BooleanField()
    street_view_control = models.BooleanField()
    style = models.TextField()
    fullscreen_control = models.BooleanField()
    map_type_control = models.CharField(max_length=255)
    rotate_control = models.BooleanField()
    scale_control = models.BooleanField()
    template = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_googlemap_googlemap'


class DjangocmsGooglemapGooglemapmarker(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField(blank=True, null=True)
    show_content = models.BooleanField()
    info_content = models.TextField()
    icon = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_googlemap_googlemapmarker'


class DjangocmsGooglemapGooglemaproute(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    title = models.CharField(max_length=255)
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_mode = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_googlemap_googlemaproute'


class DjangocmsIconIcon(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    icon = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    attributes = models.TextField()

    class Meta:
        managed = False
        db_table = 'djangocms_icon_icon'


class DjangocmsLinkLink(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    name = models.CharField(max_length=255)
    anchor = models.CharField(max_length=255)
    mailto = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    target = models.CharField(max_length=255)
    attributes = models.TextField()
    template = models.CharField(max_length=255)
    internal_link = models.ForeignKey(CmsPage, models.DO_NOTHING, blank=True, null=True)
    file_link = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)
    external_link = models.CharField(max_length=2040)

    class Meta:
        managed = False
        db_table = 'djangocms_link_link'


class DjangocmsPicturePicture(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    picture = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    attributes = models.TextField()
    caption_text = models.TextField(blank=True, null=True)
    link_attributes = models.TextField()
    link_target = models.CharField(max_length=255)
    use_automatic_scaling = models.BooleanField()
    use_crop = models.BooleanField()
    use_no_cropping = models.BooleanField()
    use_upscale = models.BooleanField()
    thumbnail_options = models.ForeignKey('FilerThumbnailoption', models.DO_NOTHING, blank=True, null=True)
    external_picture = models.CharField(max_length=255, blank=True, null=True)
    template = models.CharField(max_length=255)
    alignment = models.CharField(max_length=255)
    link_page = models.ForeignKey(CmsPage, models.DO_NOTHING, blank=True, null=True)
    use_responsive_image = models.CharField(max_length=7)
    link_url = models.CharField(max_length=2040, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_picture_picture'


class DjangocmsSnippetSnippet(models.Model):
    name = models.CharField(unique=True, max_length=255)
    html = models.TextField()
    template = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_snippet_snippet'


class DjangocmsSnippetSnippetptr(models.Model):
    snippet = models.ForeignKey(DjangocmsSnippetSnippet, models.DO_NOTHING)
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'djangocms_snippet_snippetptr'


class DjangocmsStyleStyle(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    class_name = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    padding_left = models.PositiveSmallIntegerField(blank=True, null=True)
    padding_right = models.PositiveSmallIntegerField(blank=True, null=True)
    padding_top = models.PositiveSmallIntegerField(blank=True, null=True)
    padding_bottom = models.PositiveSmallIntegerField(blank=True, null=True)
    margin_left = models.PositiveSmallIntegerField(blank=True, null=True)
    margin_right = models.PositiveSmallIntegerField(blank=True, null=True)
    margin_top = models.PositiveSmallIntegerField(blank=True, null=True)
    margin_bottom = models.PositiveSmallIntegerField(blank=True, null=True)
    additional_classes = models.CharField(max_length=255)
    attributes = models.TextField()
    id_name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    template = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'djangocms_style_style'


class DjangocmsTextCkeditorText(models.Model):
    body = models.TextField()
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'djangocms_text_ckeditor_text'


class DjangocmsVideoVideoplayer(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    embed_link = models.CharField(max_length=255)
    poster = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True)
    attributes = models.TextField()
    label = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    parameters = models.TextField()

    class Meta:
        managed = False
        db_table = 'djangocms_video_videoplayer'


class DjangocmsVideoVideosource(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    text_title = models.CharField(max_length=255)
    text_description = models.TextField()
    attributes = models.TextField()
    source_file = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_video_videosource'


class DjangocmsVideoVideotrack(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    kind = models.CharField(max_length=255)
    srclang = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    attributes = models.TextField()
    src = models.ForeignKey('FilerFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'djangocms_video_videotrack'


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.OneToOneField(EasyThumbnailsThumbnail, models.DO_NOTHING)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class FilerClipboard(models.Model):
    user = models.ForeignKey('LoginMyuser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboard'


class FilerClipboarditem(models.Model):
    clipboard = models.ForeignKey(FilerClipboard, models.DO_NOTHING)
    file = models.ForeignKey('FilerFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboarditem'


class FilerFile(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)
    field_file_size = models.BigIntegerField(db_column='_file_size', blank=True, null=True)  # Field renamed because it started with '_'.
    sha1 = models.CharField(max_length=40)
    has_all_mandatory_data = models.BooleanField()
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    is_public = models.BooleanField()
    folder = models.ForeignKey('FilerFolder', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('LoginMyuser', models.DO_NOTHING, blank=True, null=True)
    polymorphic_ctype = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    mime_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'filer_file'


class FilerFolder(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    lft = models.PositiveIntegerField()
    rght = models.PositiveIntegerField()
    tree_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    owner = models.ForeignKey('LoginMyuser', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folder'
        unique_together = (('parent', 'name'),)


class FilerFolderpermission(models.Model):
    type = models.SmallIntegerField()
    everybody = models.BooleanField()
    can_edit = models.SmallIntegerField(blank=True, null=True)
    can_read = models.SmallIntegerField(blank=True, null=True)
    can_add_children = models.SmallIntegerField(blank=True, null=True)
    folder = models.ForeignKey(FilerFolder, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('LoginMyuser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folderpermission'


class FilerImage(models.Model):
    file_ptr = models.OneToOneField(FilerFile, models.DO_NOTHING, primary_key=True)
    field_height = models.FloatField(db_column='_height', blank=True, null=True)  # Field renamed because it started with '_'.
    date_taken = models.DateTimeField(blank=True, null=True)
    default_alt_text = models.CharField(max_length=255, blank=True, null=True)
    default_caption = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    must_always_publish_author_credit = models.BooleanField()
    must_always_publish_copyright = models.BooleanField()
    subject_location = models.CharField(max_length=64)
    field_width = models.FloatField(db_column='_width', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'filer_image'


class FilerThumbnailoption(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    crop = models.BooleanField()
    upscale = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'filer_thumbnailoption'


class LoginMyuser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    phone = models.CharField(unique=True, max_length=12)
    email = models.CharField(unique=True, max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    avatar = models.TextField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    date_joined = models.DateTimeField()
    address = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'login_myuser'


class LoginMyuserGroups(models.Model):
    myuser = models.ForeignKey(LoginMyuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'login_myuser_groups'
        unique_together = (('myuser', 'group'),)


class LoginMyuserUserPermissions(models.Model):
    myuser = models.ForeignKey(LoginMyuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'login_myuser_user_permissions'
        unique_together = (('myuser', 'permission'),)


class LoginRegisterfrommessangers(models.Model):
    messenger = models.IntegerField()
    id_messenger = models.CharField(unique=True, max_length=100)
    user = models.ForeignKey(LoginMyuser, models.DO_NOTHING, blank=True, null=True)
    phone = models.CharField(unique=True, max_length=12)

    class Meta:
        managed = False
        db_table = 'login_registerfrommessangers'


class MenusCachekey(models.Model):
    language = models.CharField(max_length=255)
    site = models.PositiveIntegerField()
    key = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'menus_cachekey'


class OrdersOrder(models.Model):
    num_order = models.CharField(unique=True, max_length=64)
    order_price = models.FloatField()
    payment_state = models.BooleanField()
    contract = models.CharField(max_length=100)
    manager = models.ForeignKey(LoginMyuser, models.DO_NOTHING)
    user = models.ForeignKey(LoginMyuser, models.DO_NOTHING)
    terms_of_readiness = models.IntegerField(blank=True, null=True)
    installation_time = models.IntegerField(blank=True, null=True)
    is_cancel = models.BooleanField()
    is_notified = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'orders_order'


class OrdersStateorder(models.Model):
    date_time = models.DateTimeField()
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_stateorder'


class ReviewsReview(models.Model):
    review = models.TextField()
    is_confirm = models.IntegerField()
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    user = models.ForeignKey(LoginMyuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reviews_review'


class RollercmsBackcall(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    internal_link_wa = models.CharField(max_length=64)
    external_link_wa = models.CharField(max_length=64)
    internal_link_vi = models.CharField(max_length=64)
    external_link_vi = models.CharField(max_length=64)
    internal_link_tg = models.CharField(max_length=64)
    external_link_tg = models.CharField(max_length=64)
    text = models.TextField()

    class Meta:
        managed = False
        db_table = 'rollercms_backcall'


class RollercmsCreditandpartnership(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    image_1 = models.CharField(max_length=100)
    title_1 = models.CharField(max_length=16)
    description_1 = models.CharField(max_length=32)
    image_2 = models.CharField(max_length=100)
    title_2 = models.CharField(max_length=16)
    description_2 = models.CharField(max_length=32)
    image_3 = models.CharField(max_length=100)
    title_3 = models.CharField(max_length=16)
    description_3 = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'rollercms_creditandpartnership'


class RollercmsGallery(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'rollercms_gallery'


class RollercmsMygooglemap(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    map_src = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'rollercms_mygooglemap'


class RollercmsPhoto(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.CharField(max_length=100)
    gallery = models.ForeignKey(RollercmsGallery, models.DO_NOTHING)
    link = models.ForeignKey(CmsPage, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rollercms_photo'


class RollercmsSlider(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    gallery = models.ForeignKey(RollercmsGallery, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rollercms_slider'


class RollercmsTagline(models.Model):
    cmsplugin_ptr = models.OneToOneField(CmsCmsplugin, models.DO_NOTHING, primary_key=True)
    summary_text = models.TextField()
    tagline_title = models.CharField(max_length=64)
    tagline_subtitle = models.CharField(max_length=64)
    benefit_1_title = models.CharField(max_length=64)
    benefit_1 = models.TextField()
    benefit_2_title = models.CharField(max_length=64)
    benefit_2 = models.TextField()
    link = models.ForeignKey(CmsPage, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rollercms_tagline'
