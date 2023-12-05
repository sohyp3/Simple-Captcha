async function SendRequest(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    } catch (error) {
        throw error;
    }
}


async function SendPostRequest(url, data) {
    try {
        // const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // 'X-CSRFToken': csrf,
            },
            body: JSON.stringify(data),
        });
        const responseData = await response.json();
        return responseData;
    } catch (err) {
        console.error(err);
    }
}


async function neww() {
    cap_img = document.getElementById('cap-img')
    resp = await SendRequest('/new')
    cap_img.src = `/static/media/${resp.path}.png`
}

async function sbmt() {
    code_input = document.getElementById('code-input')
    msg = document.getElementById('msg')
    cap_img = document.getElementById('cap-img')

    data = {
        'code': code_input.value
    }

    resp = await SendPostRequest('/submit', data)

    if (resp.msg == "correct") {
        msg.hidden = false
        msg.innerText = 'Correct Welcome Abord'
        code_input.value = ''

    } else if (resp.msg == 'toomany') {
        msg.hidden = false
        msg.innerText = 'Too many incorrect attempts!'

        cap_img.src = `/static/media/${resp.path}.png`

    } else if (resp.msg == 'incorrect') {
        msg.hidden = false
        msg.innerText = 'incorrect, try again!'
    }
}

