<!--frontend/src/routes/ProfileModal.svelte-->
<script>
    export let showModal;
    export let toggleModal;

    let form = {
        username: "",
        email: "",
        password: ""
    };

    async function handleRegister(event) {
        event.preventDefault();

        const response = await fetch('http://localhost:5000/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: form.username,
                email: form.email,
                password: form.password,
            }),
        });

        if (!response.ok) {
            console.error('Response status:', response.status);
            console.error('Response headers:', response.headers);
            console.error('Response text:', await response.text());
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        console.log('User registered:', result);
    }
</script>

{#if showModal}
    <div role="dialog" aria-modal="true" class="fixed inset-0 bg-gray-800 bg-opacity-75 flex items-center justify-center z-50">
        <div class="bg-white p-4 rounded-lg shadow-lg">
            <h2 class="text-xl mb-4">Profile</h2>
            <form on:submit|preventDefault="{handleRegister}">
                <div class="mb-4">
                    <label for="username" class="block text-sm font-medium text-gray-700">Username</label>
                    <input id="username" type="text" bind:value="{form.username}" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required />
                </div>
                <div class="mb-4">
                    <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                    <input id="email" type="email" bind:value="{form.email}" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required />
                </div>
                <div class="mb-4">
                    <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
                    <input id="password" type="password" bind:value="{form.password}" class="mt-1 block w-full border border-gray-300 rounded-md p-2" required />
                </div>
                <button type="submit" class="btn variant-filled">Register</button>
            </form>
            <button on:click="{() => toggleModal(false)}" class="mt-4 btn variant-outlined">Close</button>
        </div>
    </div>
{/if}

<style>
    .btn {
        /* Add your button styles here */
    }
</style>