let changeExistingImage = function() {
    var img = '/static/background/' +  document.getElementById('chooseImage').selectedOptions[0].text
    document.getElementById('img-avatar').setAttribute('src', img)
}

let changeUploadImage = function() {
    var img = document.getElementById('uploadImage').files[0]
    document.getElementById('img-avatar').setAttribute('src', window.URL.createObjectURL(img))
    var r = new FileReader()
    var img = document.getElementById('uploadImage').files[0]
    console.log(img)
    r.readAsDataURL(img)
    r.onload = function() {
        console.log(r.result)
        sessionStorage.setItem('pic', r.result)
    }
}

let changeImageOrigin = function() {
    var ch = document.getElementById('chooseOrigin').selectedOptions[0].text
    if (ch == '上传图片') {
        changeUploadImage()
    } else {
        changeExistingImage()
    }
}

window.onload = function() {
    var submit = document.getElementById("post")
    submit.onclick = function() {
    var poemid = '/render/' + document.getElementById('poemID').value
    var ch = document.getElementById('chooseOrigin').selectedOptions[0].text
    // if (ch == '上传图片') {
    //     var r = new FileReader()
    //     var img = document.getElementById('uploadImage').files[0]
    //     console.log(img)
    //     r.readAsDataURL(img)
    //     console.log(r)
    //     sessionStorage.setItem('pic', r.result)
    // }
    document.getElementsByTagName('form')[0].setAttribute('action', poemid)
}
}
