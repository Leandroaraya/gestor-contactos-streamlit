import streamlit as st
from src.gestor import GestorContactos
from src.contacto import Contacto

st.set_page_config(
    page_title="Gestor de Contactos",
    page_icon="📇",
    layout="wide"
)

gestor = GestorContactos()

st.title("📇 Gestor de Contactos")

# ---------------- LAYOUT ----------------
col_izq, col_centro, col_der = st.columns(3)

# ================= IZQUIERDA =================
with col_izq:
    st.subheader("➕ Agregar contacto")
    with st.form("form_agregar"):
        nombre = st.text_input("Nombre")
        telefono = st.text_input("Teléfono")
        correo = st.text_input("Correo")
        direccion = st.text_input("Dirección")
        agregar = st.form_submit_button("Agregar")

    if agregar:
        if not nombre.strip() or not telefono.strip():
            st.error("Nombre y teléfono son obligatorios")
        elif not telefono.isdigit():
            st.error("El teléfono debe contener solo números")
        else:
            c = Contacto(nombre, telefono, correo, direccion)
            if gestor.agregar_contacto(c):
                st.success("Contacto agregado")
                st.rerun()
            else:
                st.error("Contacto duplicado")

    st.divider()

    st.subheader("🗑️ Eliminar contacto")
    if gestor.contactos:
        opciones = [str(c) for c in gestor.contactos]
        seleccionado = st.selectbox("Selecciona un contacto", opciones)

        if st.button("Eliminar contacto"):
            contacto = gestor.contactos[opciones.index(seleccionado)]
            gestor.eliminar_contacto(contacto)
            st.success("Contacto eliminado")
            st.rerun()
    else:
        st.info("No hay contactos para eliminar")


# ================= CENTRO =================
with col_centro:
    st.subheader("🔍 Buscar contacto")
    texto = st.text_input("Buscar por nombre o teléfono")

    if texto:
        resultados = gestor.buscar_contacto(texto)
        if resultados:
            for c in resultados:
                st.write(c)
        else:
            st.warning("No se encontraron contactos")

    st.divider()

    st.subheader("✏️ Editar contacto")

    if gestor.contactos:
        opciones = [str(c) for c in gestor.contactos]
        seleccionado = st.selectbox("Contacto a editar", opciones, key="editar")

        contacto = gestor.contactos[opciones.index(seleccionado)]

        with st.form("form_editar"):
            nuevo_nombre = st.text_input("Nombre", contacto.nombre)
            nuevo_telefono = st.text_input("Teléfono", contacto.telefono)
            nuevo_correo = st.text_input("Correo", contacto.correo)
            nueva_direccion = st.text_input("Dirección", contacto.direccion)
            guardar = st.form_submit_button("Guardar cambios")

        if guardar:
            contacto.actualizar(
                nombre=nuevo_nombre,
                telefono=nuevo_telefono,
                correo=nuevo_correo,
                direccion=nueva_direccion
            )
            gestor.guardar_contactos()
            st.success("Contacto actualizado")
            st.rerun()
    else:
        st.info("No hay contactos para editar")


# ================= DERECHA =================
with col_der:
    st.subheader("📋 Lista de contactos")
    if gestor.contactos:
        for c in gestor.contactos:
            st.write(c)
    else:
        st.info("No hay contactos registrados")
    
