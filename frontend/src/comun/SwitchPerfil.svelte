<script lang="ts">
    // @ts-ignore //For importing .ts files
    type ClickHandler = (nuevoPerfil: string) => () => void;

    const cambiarPerfil: ClickHandler = (nuevoPerfil) => async () => {

        let perfil = await fetch("/api/greet").then((res) => res.json());
        localStorage.setItem("perfil", nuevoPerfil);
        
        location.reload()
    };
</script>


{#if localStorage.getItem("perfil") === "3"}
    <div id="upperRelay">
        <div class="switch">
            <button on:click|once={cambiarPerfil("1")} id="btnAlumnoPerfil"> Alumno</button>
            <button on:click|once={cambiarPerfil("2")} id="btnColaboradorPerfil"> Colaborador</button>
        </div>

    </div>
{/if}

            
<button on:click|once={cambiarPerfil("3")}> DEBUG, RESET a 3 </button>


<style>
    #upperRelay{
        height: 100%;
        position: absolute;
        width: 100%;
        z-index: 100;
        background-color: rgba(0, 0, 0, 0.9);
        backdrop-filter: blur(5px);
    }

    .switch{
        display: grid;
        gap: 5rem;
        grid-template-columns: repeat(2, 1fr);
        z-index: 100;
        margin: 0 5%;
       /* grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));*/
        align-items: center;
        height: 100%;
        min-width: 300px;
    }

    button{
        border:none;
        color:white;
        padding: 10px 0px;
        cursor: pointer;
    }

    button:hover, button:focus {
        filter: brightness(0.55)
    }
    
    #btnAlumnoPerfil{
        background-color: #FF5900;
    }

    #btnColaboradorPerfil{
        background-color:#362453 
    }
    
    

</style>
