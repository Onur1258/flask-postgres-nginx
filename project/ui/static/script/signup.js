async function signup() {
    const firstname= document.getElementById("firstname").value;
    const middlename = document.getElementById("middlename").value;
    const lastname = document.getElementById("lastname").value;
    const user_name = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const email = document.getElementById("email").value;
    const birthdate = document.getElementById("birthdate").value;
    const url = '/user/create';
    const new_user = {
        username:user_name,
        firstname:firstname,
        middlename:middlename,
        lastname:lastname,
        birthdate:birthdate,
        email:email,
        password:password
    }
    await fetch(url,{
        method: 'POST',
        headers: {
				'Accept': 'application/json',
        		'Content-Type': 'application/json'
			},
        body: JSON.stringify(new_user)
    })
        .then(async response => {
            console.log(response)
            if (response.ok) {
                return response.json()
                    .then(successMessage => {
                        if(!alert(successMessage['message'])){
                            window.location.href = 'http://192.168.0.182:5000/';
                        }
                    });
            } else {
               return response.json()
                   .then(errorMessage => {
                       throw new Error(errorMessage['message'])
                   });
            }
        })
        .catch(error => {
            alert(error['message'])
        });
}
function goBack(){
    window.location.href = '/';
}