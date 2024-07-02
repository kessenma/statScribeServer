<script>
    export let showModal;
    export let toggleModal;
</script>

{#if showModal}
    <div role="dialog" aria-modal="true" class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-50" on:click="{() => toggleModal(false)}" on:keydown="{e => e.key === 'Escape' && toggleModal(false)}" tabindex="0">
        <div class="bg-white p-4 rounded-lg shadow-lg" on:click|stopPropagation>
            <h2 class="text-xl mb-4">Profile</h2>
            <button class="btn variant-filled" on:click="{() => alert('Login button clicked!')}">Login</button>
        </div>
    </div>
{/if}

<style>
    .btn {
        /* Add your button styles here */
    }
</style>
