from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("perfil/", views.perfil_user, name="perfil"),
    path("logout/", views.logout_view, name="logout"),
    path("publicar-oferta/", views.publicar_oferta, name="publicar_oferta"),
    path("ofrecer-servicio/", views.ofrecer_servicio, name="ofrecer_servicio"),
    path("publicar/", views.publicar_estado, name="publicar_estado"),
    path("like/<int:publicacion_id>/", views.like_toggle, name="like_toggle"),
    path("comentar/<int:publicacion_id>/", views.comentar, name="comentar"),
    path(
        "comentarios/<int:publicacion_id>/",
        views.listar_comentarios,
        name="listar_comentarios",
    ),
    path("empleos/", views.empleos, name="empleos"),
    path("trabajadores/", views.trabajadores, name="trabajadores"),
    path(
        "api/oferta/<int:oferta_id>/",
        views.api_oferta_detalle,
        name="api_oferta_detalle",
    ),
    path(
        "api/servicio/<int:servicio_id>/",
        views.api_servicio_detalle,
        name="api_servicio_detalle",
    ),
    path("perfil/cambiar-foto/", views.cambiar_foto, name="cambiar_foto"),
    path("perfil/editar-campo/", views.editar_campo, name="editar_campo"),
    path(
        "perfil/toggle-disponibilidad/",
        views.toggle_disponibilidad,
        name="toggle_disponibilidad",
    ),
    path("perfil/editar-perfil/", views.editar_perfil, name="editar_perfil"),
    path("perfil/subir-portafolio/", views.subir_portafolio, name="subir_portafolio"),
    path(
        "perfil/eliminar-portafolio/<int:foto_id>/",
        views.eliminar_portafolio,
        name="eliminar_portafolio",
    ),
    path("api/buscar-ajax/", views.api_buscar_ajax, name="api_buscar_ajax"),
    path(
        "perfil-trabajador/<int:trabajador_id>/",
        views.perfil_trabajador_publico,
        name="perfil_trabajador_publico",
    ),
    path("calificar/", views.calificar_usuario, name="calificar_usuario"),
    path(
        "api/calificaciones/<int:usuario_id>/",
        views.obtener_calificaciones,
        name="obtener_calificaciones",
    ),
    path(
        "api/mis-calificaciones/", views.mis_calificaciones, name="mis_calificaciones"
    ),
    path("recuperar-password/", views.recuperar_password, name="recuperar_password"),
    path(
        "reset-password/<uidb64>/<token>/", views.reset_password, name="reset_password"
    ),
    path("mapa/", views.mapa, name="mapa"),
    path("api/ubicaciones/", views.api_ubicaciones, name="api_ubicaciones"),
    path("api/todos-trabajadores/", views.api_todos_trabajadores, name="api_todos_trabajadores"),
]
