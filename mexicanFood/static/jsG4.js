import Swal from "https://unpkg.com/sweetalert/dist/sweetalert.min.js" 

// var json = localStorage.getItem("array");
// let integrante= [{name:"Julio Santillan",email:"jsantillan@example.com"}, 
//     {name:"Blanca Hidalgo",email:"bhidalgo@example.com"}, 
//     {name:"Jorge Freire",email:"jfreire@example.com"},
//     {name:"Alexandra Morales",email:"amorales@example.com"},
//     {name:"Alexander Morales",email:"amorales@example.com"}];

// if (json != null) { 
//     integrante = JSON.parse(json);

// }

// function obtenerDatos(){
//     let nombre = document.getElementById("nombre").value;
//     let correo = document.getElementById("email").value;
    
//     integrante.push({name:nombre,email:correo});  
//     localStorage.setItem("array", JSON.stringify(integrante));
    
      
// }

// function eliminarIntegrante(cardNumber){
    
//     integrante.splice(cardNumber, 1);
//     localStorage.setItem("array", JSON.stringify(integrante));   
//     generarContenidoHTML();
// }

// function generarContenidoHTML(){
   
//     let html = '<div class="d-flex justify-content-around separation">';
//     let cantidadTarjetas= 0;
//     for (let i = 0; i < integrante.length; i++) {
//         cantidadTarjetas++;
//         html +=`<div class="card" style="width:20%">
//                     <img class="card-img-top" src="static/img/person${i+1}.jpg" alt="Card image">
//                     <div class="card-body">
//                     <h4 class="card-title" id="cardTitle" style="color: black">${integrante[i].name}</h4>
//                     <p class="card-text" style="color: black">${integrante[i].email}</p>
//                     <a href="#" class="btn btn-danger" onclick="eliminarIntegrante(${i})">Eliminar</a>
//                     </div>
//                 </div>`;
//         if (cantidadTarjetas % 4 == 0){
//             html += `</div>
//                     <div class="d-flex justify-content-around separacion">`
//         }
//     }
//     html += '</div>';
//     document.getElementById("infTeam").innerHTML = html;
   
// }


