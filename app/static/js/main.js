function showToast(message, type="success") {
    const container = document.getElementById("toast-container");

    const toast = document.createElement("div");
    toast.classList.add("toast", type);
    toast.textContent = message;

    container.appendChild(toast);

    setTimeout(() => toast.classList.add("show"), 10);

    setTimeout(() => {
        toast.classList.remove("show");
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}

function handleFavorite(btn) {
    let id = btn.dataset.id;

    fetch(`/toggle-fav/${id}`, { method: "POST" })
    .then(res => res.json())
    .then(data => {
        if (data.is_fav) {
            btn.innerHTML = "💝";
            showToast("Marked as Favorites ✅")
        } else {
            btn.innerHTML = "🩶";
            showToast("Unmarked as Favorites 💔")
        }
    });
}

function handleComplete(btn){
    let id = btn.dataset.id ;

    fetch(`/toggle-completed/${id}` , {method  :"POST"})
    .then(res => res.json()).then(data => {

        let card = btn.closest(".Content") ;
        card.classList.toggle("done") ;
        if(data.is_completed){
            btn.innerHTML = "🟢" ;
            showToast("Marked as Completed ✅") ;
        }else{
            btn.innerHTML = "🔴" ; 
            showToast("Unmarked from completed ") ;
        }
    });
}
