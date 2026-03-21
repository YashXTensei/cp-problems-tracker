function showToast(message, type = "success") {
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

async function handleFavorite(btn) {
    let id = btn.dataset.id;

    try {
        const res = await fetch(`/toggle-fav/${id}`, { method: "POST" });
        const data = await res.json();

        if (data.is_fav) {
            btn.innerHTML = "💝";
            showToast("Marked as Favorites ✅");
        } else {
            btn.innerHTML = "🩶";
            showToast("Unmarked as Favorites 💔");
        }

    } catch (err) {
        showToast("Network error! 😵", "error");
    }
}

async function handleComplete(btn) {
    let id = btn.dataset.id;

    try {
        const res = await fetch(`/toggle-completed/${id}`, { method: "POST" });
        const data = await res.json();

        let card = btn.closest(".Content");
        card.classList.toggle("done");

        if (data.is_completed) {
            btn.innerHTML = "🟢";
            showToast("Marked as Completed ✅");
        } else {
            btn.innerHTML = "🔴";
            showToast("Unmarked from completed");
        }

    } catch (err) {
        showToast("Network error! 😵", "error");
    }
}

async function handleDelete(btn) {
    const confirmed = confirm("Are you sure you want to delete this ?");
    if (!confirmed) return;

    const id = btn.dataset.id;

    try {
        const res = await fetch(`/delete/${id}`, { method: "POST" });
        const data = await res.json();

        if (data.status === "success") {
            btn.closest(".Content").remove();
            showToast("Deleted Successfully 👌");
        }
    } catch (err) {
        showToast("Delete failed! 😵", "error");
    }
}