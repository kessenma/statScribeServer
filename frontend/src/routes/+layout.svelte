<script lang="ts">
	import '../app.postcss';
	import { AppShell, AppBar } from '@skeletonlabs/skeleton';
	import ProfileModal from './ProfileModal.svelte';

	// Highlight JS
	import hljs from 'highlight.js/lib/core';
	import 'highlight.js/styles/github-dark.css';
	import { storeHighlightJs } from '@skeletonlabs/skeleton';
	import xml from 'highlight.js/lib/languages/xml'; // for HTML
	import css from 'highlight.js/lib/languages/css';
	import javascript from 'highlight.js/lib/languages/javascript';
	import typescript from 'highlight.js/lib/languages/typescript';

	hljs.registerLanguage('xml', xml); // for HTML
	hljs.registerLanguage('css', css);
	hljs.registerLanguage('javascript', javascript);
	hljs.registerLanguage('typescript', typescript);
	storeHighlightJs.set(hljs);

	// Floating UI for Popups
	import { computePosition, autoUpdate, flip, shift, offset, arrow } from '@floating-ui/dom';
	import { storePopup } from '@skeletonlabs/skeleton';
	storePopup.set({ computePosition, autoUpdate, flip, shift, offset, arrow });

	let showModal = false;

	function toggleModal(state) {
		showModal = state;
	}
</script>

<!-- App Shell -->
<AppShell>
	<svelte:fragment slot="header">
		<!-- App Bar -->
		<AppBar>
			<svelte:fragment slot="lead">
				<strong class="text-xl">StatScribe</strong>
			</svelte:fragment>
			<svelte:fragment slot="trail">
				<a class="btn btn-sm variant-ghost-surface" href="/">
					Home
				</a>
				<a class="btn btn-sm variant-ghost-surface" href="/analysis">
					Analysis
				</a>
				<a class="btn btn-sm variant-ghost-surface" href="/history">
					History
				</a>
				<a class="btn btn-sm variant-ghost-surface" href="/signout">
					Sign out
				</a>
				<!-- Profile Icon -->
				<button class="profile-icon" on:click="{() => toggleModal(true)}">
					<!-- Profile Icon (You can use an SVG or FontAwesome icon) -->
					<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-8 h-8">
						<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5.121 17.804A9.001 9.001 0 1112 21a9.001 9.001 0 01-6.879-3.196M12 7v4m0 4h.01M12 7h.01" />
					</svg>
				</button>
			</svelte:fragment>
		</AppBar>
	</svelte:fragment>
	<!-- Page Route Content -->
	<slot />
	<!-- Profile Modal -->
	<ProfileModal {showModal} {toggleModal} />
</AppShell>

<style>
	.profile-icon {
		cursor: pointer;
	}
</style>
