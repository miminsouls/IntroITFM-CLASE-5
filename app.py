import streamlit as st
from PIL import Image

st.title("THE TORTURED")

st.header(" ⓘㅤcada historia aquí escrita está manchada de sangre, un testimonio de almas condenadas y cicatrices invisibles. bienvenides a las escrituras de los torturados.")
st.write("𝘀𝗶𝗲́𝗻𝘁𝗮𝗻𝘀𝗲 𝗲𝗻 𝗰𝗮𝘀𝗮. 𝘀𝗶 𝗲𝘀 𝗾𝘂𝗲 𝗲𝗻 𝗲𝗹 𝗶𝗻𝗳𝗶𝗲𝗿𝗻𝗼 𝗵𝗮𝘆 𝗮𝗹𝗴𝗼 𝗰𝗼𝗺𝗼 𝗲𝘀𝗼.")
image = Image.open("WhatsApp Image 2025-02-27 at 10.03.49.jpeg")

st.image (image, caption="THE TORTURED ONES")

texto = st.text_input("Escribe algo", "Este es un texto")
st.write("El texto escrito es", texto)


st.subheader("Personajes")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las Interfaces Multimodales mejoraan la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("Correcto!")

with col2:
  st.subheader("Esta es las egunda columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("Visual", "Auditiva", "Tactil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audicion es fundamental para tu interfaz")
  if modo == "Tactil":
    st.write("El tacto es fundamental para tu interfaz")

st.subheader("Uso de botones")
if st.button("Presiona el boton"):
  st.write("Gracias por presionar")
else:
  st. write("No has presionado aun")

st.subheader("Selectbox")
in_mod = st.selectbox(
  "Selecciona la modalidad",
  ("Audio", "Visual", "Haptico"),
)
if in_mod === "Audio":
  set_mod = "Reproducir audio"
elif in_mod == "Visual":
  set_mod = "Reproducir video"
elif in_mod == "Haptico":
  set_mod = "Activar vibracion"
st.write("La accion es:", set_mod)

with st.sidebar:
  st.subheader("Configura la modalidad")
