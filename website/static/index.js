const btn = document.getElementById("checkbox")
btn.addEventListener("change", () => {
  document.body.classList.toggle("dark")
})

function deleteNode(noteID){
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteID: noteID}),
    }).then((_res) => {
        window.location.href = "/";
    })
}