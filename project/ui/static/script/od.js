
async function loadOnlineUsers() {
    let url = '/onlineusers';
    await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok){
                response.json()
                    .then(items => {
                        const table = document.getElementById("tableBody");
                        for (let i = 0; i < items.length; i++) {
                            let row = table.insertRow();
                            let id = row.insertCell(0);
                            let username = row.insertCell(1);
                            let ipaddr = row.insertCell(2);
                            let timestamp = row.insertCell(3);
                            id.innerHTML = items[i].id;
                            username.innerHTML = items[i].username;
                            ipaddr.innerHTML = items[i].ipaddress;
                            timestamp.innerHTML = items[i].logindatetime;
                        }
                    })
            }
        });
}

async function getLogs() {
    let url = '/logs';
    await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok){
                response.json()
                    .then(items => {
                        console.log(items)
                        const obj = JSON.parse(items)
                        console.log(obj)
                        download(items, "Logs", "text/plain")
                    })
            }
        });
}
function download(content, fileName, contentType) {
		  const a = document.createElement("a");
		  const file = new Blob([content], { type: contentType });
		  a.href = URL.createObjectURL(file);
		  a.download = fileName;
		  a.click();
		}
async function loadUsers() {
    let url = '/user/list';
    await fetch(url, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
    })
        .then(response => {
            if (response.ok){
                response.json()
                    .then(items => {
                        const table = document.getElementById("userTableBody");
                        for (let i = 0; i < items.length; i++) {
                            let row = table.insertRow();
                            let id = row.insertCell(0);
                            let username = row.insertCell(1);
                            let firstname = row.insertCell(2);
                            let middlename = row.insertCell(3);
                            let lastname = row.insertCell(4);
                            let email = row.insertCell(5);
                            let birthdate = row.insertCell(6);
                            id.innerHTML = items[i].id;
                            username.innerHTML = items[i].username;
                            firstname.innerHTML = items[i].firstname;
                            middlename.innerHTML = items[i].middlename;
                            lastname.innerHTML = items[i].lastname;
                            email.innerHTML = items[i].email;
                            birthdate.innerHTML = items[i].birthdate
                        }
                    })
            }
        });
}