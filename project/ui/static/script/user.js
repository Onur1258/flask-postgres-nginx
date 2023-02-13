function getDogPic() {
    var btn = document.querySelector("button");
    var display = document.querySelector("#display");
    btn.addEventListener("click", function(){
    var XHR = new XMLHttpRequest();
    XHR.onreadystatechange = function() {
        if (XHR.readyState == 4 && XHR.status == 200) {
            var n = JSON.parse(XHR.responseText);
            console.log(n.message);
            display.src = n.message;
        }
    };
    var url = "https://dog.ceo/api/breeds/image/random"
    XHR.open("GET", url);
    XHR.send();
    })
}

async function logout() {
    let username = localStorage.getItem("currentUser");
    const url = "/logout"
    const user_data = {
        username: username
    };
    await fetch(url, {
        method: 'DELETE',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(user_data)
    })
        .then(response => {
           if(response.ok){
               localStorage.removeItem("currentUser")
               window.location.href =  '/';
           }
        });
}