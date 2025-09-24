// Lógica del desafío: Amigo Secreto
// Array para almacenar los nombres
const amigos = [];

// Agregar un amigo desde el input
function agregarAmigo() {
  const input = document.getElementById("amigo");
  const nombre = (input?.value || "").trim();

  if (!nombre) {
    alert("Por favor, escribe un nombre.");
    input?.focus();
    return;
  }

  // Evitar duplicados (ignorando mayúsculas/minúsculas)
  const existe = amigos.some(a => a.toLowerCase() === nombre.toLowerCase());
  if (existe) {
    alert("Ese nombre ya está en la lista.");
    input.value = "";
    input.focus();
    return;
  }

  amigos.push(nombre);
  input.value = "";
  input.focus();
  actualizarLista();
}

// Actualizar la lista de amigos en el DOM
function actualizarLista() {
  const lista = document.getElementById("listaAmigos");
  const resultado = document.getElementById("resultado");
  if (!lista) return;

  // Limpiar listado y resultado previo
  lista.innerHTML = "";
  if (resultado) resultado.innerHTML = "";

  // Pintar cada amigo
  amigos.forEach((nombre, idx) => {
    const li = document.createElement("li");
    li.textContent = `${idx + 1}. ${nombre}`;
    lista.appendChild(li);
  });
}

// Sortear un amigo aleatoriamente
function sortearAmigo() {
  const resultado = document.getElementById("resultado");
  if (amigos.length < 2) {
    if (resultado) resultado.textContent = "Agrega al menos 2 amigos para sortear.";
    return;
  }

  const indice = Math.floor(Math.random() * amigos.length);
  const elegido = amigos[indice];
  if (resultado) {
    resultado.innerHTML = `🎉 Tu amigo secreto es: <strong>${elegido}</strong>`;
  }
}

// Exponer funciones al ámbito global para soportar onClick en el HTML
window.agregarAmigo = agregarAmigo;
window.sortearAmigo = sortearAmigo;
window.actualizarLista = actualizarLista;

// Mejora UX: presionar Enter en el input agrega el nombre
document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("amigo");
  if (input) {
    input.addEventListener("keyup", (e) => {
      if (e.key === "Enter") agregarAmigo();
    });
  }
});
