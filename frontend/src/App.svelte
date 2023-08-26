<script lang="ts">
	
	import Footer from "./comun/Footer.svelte";
	import PermisosAlumno from "./alumno/Permisos.svelte";
	import PermisosColaborador from "./colaborador/Permisos.svelte";

	import SwitchPerfil from "./comun/SwitchPerfil.svelte";
	import {onMount} from "svelte";

	let apimessage = "Waiting for server...";
	
	onMount(async () => {
		let resp = await fetch("/api/greet").then((res) => res.json());
		console.log(resp);
		apimessage = JSON.stringify(resp);
	});

</script>

<svelte:head>
  <style src="../public/global.css"></style>
    
</svelte:head>

<main>
	
	<SwitchPerfil/>


	{#if localStorage.getItem("perfil") === "1"}
		<PermisosAlumno/>
	{:else}
		{#if localStorage.getItem("perfil") === "2"}
			<PermisosColaborador/>
		{:else}
			<p> Algo ha ocurrido , Sesión incorrecta :'( </p>
		{/if}
	{/if}


	<Footer/>
</main>

<style>
	p {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
</style>