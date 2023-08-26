import { writable } from "svelte/store";


//Asignar el perfil necesario
if(localStorage.getItem("perfil") === null){
    localStorage.setItem("perfil", "3")
}

//localStorage.setItem("perfil", "3")

const storedperfil = localStorage.getItem("perfil");
export const perfil = writable(storedperfil);
	
