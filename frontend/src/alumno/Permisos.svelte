<script lang="ts">
    
	import { Router, Link, Route } from "svelte-routing";
	
	import Error404 from "./../comun/Error.svelte";
  import Inicio from "./../Inicio.svelte";

</script>


<div>
    <Router>

        <nav>
          <Link to="/">Perfil</Link>
          <Link to="about">About</Link>
          <Link to="blog">Blog</Link>
          <a href="logout/"> Salir</a>

        </nav>

        <div>
            
          <Route path="/"><Inicio /></Route>

          <Route path="*/"><Error404 /></Route>
        </div>
      </Router>

</div>
