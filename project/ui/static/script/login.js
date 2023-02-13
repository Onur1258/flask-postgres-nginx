async function login() {
		const user_name = document.getElementById("user_name").value;
		const password = document.getElementById("pass").value;
		const url = '/login';
		const user_data = {
			username:user_name,
			password:password
		};
		await fetch(url, {
			method: 'POST',
			headers: {
				'Accept': 'application/json',
        		'Content-Type': 'application/json'
			},
			body: JSON.stringify(user_data)
		})
				.then(response => {
					if (!response.ok) {
						return response.json()
							.then(errorMessage => {
								throw new Error(errorMessage['message'])
							})
							.catch(error => {
								window.alert(error)
							});
					}
					else{
						return response.json()
							.then(data => {
								let isAdmin = data['isAdmin'];
								localStorage.setItem("currentUser", user_name);
								if(isAdmin){
									window.location.href = 'adminOD';
								}
								else {
									window.location.href =  '/spectacular/page';
								}
							});
					}
				})
	}

	async function signup() {
		window.location.href =  '/signup';
	}