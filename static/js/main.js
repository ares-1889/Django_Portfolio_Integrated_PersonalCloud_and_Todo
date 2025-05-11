let credentials_field = document.getElementById('credentials-field')
let username_field = document.getElementById('username-field')
let password_field = document.getElementById('password-field')

credentials_field.addEventListener('keydown', async (e)=> {
    if (e.key === 'Enter') {
        e.preventDefault()
        let username = username_field.value
        let password = password_field.value
        let response = await fetch('api/validate',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })
        let result = await response.json()

        if (result.status === 'success') {
            // window.open('/router', '_self')
             window.location.href = '/router/'
        }
        else {
            alert('Invalid credentials')
        }
    }
}
)
