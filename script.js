/* UPLOAD CERTIFICATE */
function uploadCertificate(){
    alert("Button clicked");
    document.getElementById("certificateUpload").click();
}

function loadCertificate(event){

    let file = event.target.files[0];

    if(file){

        let reader = new FileReader();

        reader.onload = function(e){

            document.getElementById("uploadedCertificate").src = e.target.result;

            document.getElementById("uploadedCertificate").style.display = "block";

        }

        reader.readAsDataURL(file);

    }
}


/* TEMPLATE LOAD (NEW ADD) */
function loadTemplate(imageName){

    // template section hide
    document.getElementById("templates").style.display = "none";

    // editor section show
    document.getElementById("editor").style.display = "block";

    // background image set
    document.getElementById("bgImage").src = "images/" + imageName;
}