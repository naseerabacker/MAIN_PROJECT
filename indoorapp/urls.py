from django.urls import path

from indoorapp import views

urlpatterns = [
    path('login/', views.login_fun),

    path('login_post/', views.login_post),

    path('mainpage/', views.mainpage),
    path('mainpage/', views.mainpage),

    path('admin_ind/', views.admin_ind),
    path('shop_ind/', views.shop_ind),

    path('shop_profile/', views.shop_profile, name='shop_profile'),

    path('admin_add_floor/', views.admin_add_floor),
    path('admin_add_floor_post/', views.admin_add_floor_post),

    path('admin_delete_floor/<int:id>', views.admin_delete_floor, name='admin_delete_floor'),


    path('admin_edit_floor/<str:did>', views.admin_edit_floor, name='admin_edit_floor'),
    path('admin_edit_floor_post/', views.admin_edit_floor_post),

    path('admin_add_hotspot/', views.admin_add_hotspot),
    path('admin_add_hotspot_post/', views.admin_add_hotspot_post),

    path('admin_edit_hotspot/', views.admin_edit_hotspot),
    path('admin_edit_hotspot_post/', views.admin_edit_hotspot_post),


    path('floor_shop/<int:id>', views.floor_shop,name='floor_shop'),

    # path('search/', views.search,name='search'),

    path('admin_view_floor/', views.admin_view_floor),
    # path('admin_view_floor_post/', views.admin_view_floor_post),
    path('admin_delete_floor/<int:id>', views.admin_delete_floor,name='admin_delete_floor'),
    # path('admin_view_floor_post/', views.admin_view_floor_post),

    path('admin_view_hotspot/', views.admin_view_hotspot),
    # path('admin_view_hotspot_post/', views.admin_view_hotspot_post),

    path('admin_view_complaint/', views.admin_view_complaint),
    # path('admin_view_complaint_post/', views.admin_view_complaint_post),

    path('view_floor/', views.view_floor),
    path('view_query/', views.view_query),
    path('reply_query/<id>', views.reply_query),
    path('reply_query_post/', views.reply_query_post),

    path('admin_view_feedback/', views.admin_view_feedback),
    path('view_feedback/', views.view_feedback),

    path('cus_post_complaint/', views.cus_post_complaint),
    path('cus_post_complaint_post/', views.cus_post_complaint_post),

    path('cus_send_feedbk/', views.cus_send_feedbk),
    path('cus_send_feedbk_post/', views.cus_send_feedbk_post),

    path('change_pass/', views.change_pass),
    path('change_pass_post/', views.change_pass_post),

    path('signup/', views.signup),
    path('signup_post/', views.signup_post),

    path('view_offer/', views.view_offer),

    path('view_product/', views.view_product),
    path('shop_view_product/', views.shop_view_product),



    path('admin_add_shop/', views.admin_add_shop),
    path('admin_add_shop_post/', views.admin_add_shop_post),


    path('view_shop/', views.view_shop, name='view_shop'),

    path('view_shops/', views.view_shops,name='view_shops'),
    # path('view_category/', views.view_category),
    path('admin_delete_shop/<int:id>', views.admin_delete_shop, name='admin_delete_shop'),

    path('view_shop_detail/<str:did>', views.view_shop_detail,name='view_shop_detail'),
    path('view_shop_detail_admin/<str:did>', views.view_shop_detail_admin, name='view_shop_detail_admin'),

    path('admin_view_shops/',views.admin_view_shops),

    path('admin_edit_shops/<str:did>',views.admin_edit_shops,name='admin_edit_shops'),
    path('admin_edit_shops_post/',views.admin_edit_shops_post),

    path('add_product/', views.add_product),
    path('add_product_post/', views.add_product_post),

    path('add_direction/', views.add_direction),
    path('add_direction_post/', views.add_direction_post),

    path('view_direction/', views.view_direction),


    path('edit_profile/<int:did>', views.edit_profile,name='edit_profile'),
    path('edit_profile_post/', views.edit_profile_post),

    path('send_notifi/', views.send_notifi),
    path('send_notifi_post/', views.send_notifi_post),

    path('view_notifi/', views.view_notifi, name='view_notifi'),


    # =============
# ANDROID
#     =============

    path('android_login_post/', views.android_login_post),
    path('android_signup_post/', views.android_signup_post),

    path('my_find/', views.my_find),
    path("cus_view_shop/", views.cus_view_shop),
    path("cus_view_shop_post/", views.cus_view_shop_post),
    path("cus_view_shop_floor/", views.cus_view_shop_floor),
    path("cus_view_floor/", views.cus_view_floor),
    path("cus_view_direction/", views.cus_view_direction),

    path("shop_view/", views.shop_view),
    path("send_feedback/", views.send_feedback),
    path("send_query/", views.send_query),
    path("logout/", views.logout),
    path("view_query_reply/", views.view_query_reply),

]