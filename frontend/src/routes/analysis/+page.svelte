<script lang="ts">
    import { superForm } from 'sveltekit-superforms/client';
    import SuperDebug from 'sveltekit-superforms/client/SuperDebug.svelte';
    import { z } from 'zod';

    const schema = z.object({
        sourceCitation: z.boolean(),
        publicationName: z.boolean(),
        publicationYear: z.boolean(),
        publicationType: z.boolean(),
        articleAbstract: z.boolean(),
        hypotheses: z.boolean(),
        sampleSize: z.boolean(),
        meanAge: z.boolean(),
        ageStdDev: z.boolean(),
        numFemales: z.boolean(),
        countryOrigin: z.boolean(),
        sampleType: z.boolean(),
        educationLevel: z.boolean(),
        raceEthnicity: z.boolean(),
        researchMethod: z.boolean(),
        studySetting: z.boolean(),
        taskDescription: z.boolean(),
        taskDuration: z.boolean(),
        otherStatistics: z.boolean(),
        extractAll: z.boolean(),
    });

    const { form, errors, enhance, message } = superForm(schema, {
        dataType: 'json',
        taintedMessage: null,
    });
    let files = [];

    function handleFiles(event) {
        files = event.target.files || event.dataTransfer.files;
        $form.files = files; // Update form state with the selected files
    }

    function handleDragOver(event) {
        event.preventDefault();
    }
</script>

<style>
    .form-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    .submit-button {
        margin-top: 20px;
    }
    .disabled-checkbox {
        opacity: 0.5;
        pointer-events: none;
    }
    .separator {
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        margin-top: 20px;
        margin-bottom: 20px;
        width: 100%;  /* Make sure it spans the full width */
    }

    .separator-quarter-length {
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        margin-top: 20px;
        margin-bottom: 20px;
        width: 25%;  /* Make sure it spans the full width */
    }

    .file-drop-area {
        border: 2px dashed #ccc;
        padding: 20px;
        text-align: center;
        margin: 20px;
        cursor: pointer;
    }
    label {
        display: flex;
        align-items: center;
        justify-content: space-between;
        width: 10%; /* Ensure labels use full container width */
        margin: 5px;
        font-size: 16px;
    }

    .toggle-label {
        width: 10%; /* Match the width of other form elements */
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .toggle {
        position: relative;
        display: inline-block;
        width: 50px;
        height: 24px;
        margin: 5px;
    }

    .toggle input {
        opacity: 0;
        width: 0;
        height: 0;
    }

    .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #ccc;
        transition: .4s;
        border-radius: 24px;
    }

    .slider:before {
        position: absolute;
        content: "";
        height: 18px;
        width: 18px;
        left: 3px;
        bottom: 3px;
        background-color: white;
        transition: .4s;
        border-radius: 50%;
    }

    input:checked + .slider {
        background-color: #2196F3;
    }

    input:checked + .slider:before {
        transform: translateX(26px);
    }
</style>

<div class="space-y-10 text-center flex flex-col items-center">
    <h2 class="h2">Analysis</h2>
    <p>Select the following statistics and values you'd like exported from the paper:</p>
</div>

<form use:enhance method="POST" class="form-container">
    <div class="file-drop-area" on:drop={handleFiles} on:dragover={handleDragOver}>
        Drag and drop PDF files here, or click to select files
        <input type="file" multiple on:change={handleFiles} style="display: none;">
    </div>

    <hr class="separator">

    <label>
        <input type="checkbox" name="sourceCitation" bind:checked={$form.sourceCitation} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Source Citation
    </label>
    <label>
        <input type="checkbox" name="publicationName" bind:checked={$form.publicationName} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Publication Name
    </label>
    <label>
        <input type="checkbox" name="publicationYear" bind:checked={$form.publicationYear} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Publication Year
    </label>
    <label>
        <input type="checkbox" name="publicationType" bind:checked={$form.publicationType} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Publication Type
    </label>
    <label>
        <input type="checkbox" name="articleAbstract" bind:checked={$form.articleAbstract} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Article Abstract
    </label>
    <label>
        <input type="checkbox" name="hypotheses" bind:checked={$form.hypotheses} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Hypotheses
    </label>
    <label>
        <input type="checkbox" name="sampleSize" bind:checked={$form.sampleSize} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Sample Size
    </label>
    <label>
        <input type="checkbox" name="meanAge" bind:checked={$form.meanAge} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Mean Age
    </label>
    <label>
        <input type="checkbox" name="ageStdDev" bind:checked={$form.ageStdDev} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Age Standard Deviation
    </label>
    <label>
        <input type="checkbox" name="numFemales" bind:checked={$form.numFemales} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Number of Females
    </label>
    <label>
        <input type="checkbox" name="countryOrigin" bind:checked={$form.countryOrigin} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Country of Origin
    </label>
    <label>
        <input type="checkbox" name="sampleType" bind:checked={$form.sampleType} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Sample Type
    </label>
    <label>
        <input type="checkbox" name="educationLevel" bind:checked={$form.educationLevel} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Education Level
    </label>
    <label>
        <input type="checkbox" name="raceEthnicity" bind:checked={$form.raceEthnicity} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Race or Ethnicity
    </label>
    <label>
        <input type="checkbox" name="researchMethod" bind:checked={$form.researchMethod} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Research Method
    </label>
    <label>
        <input type="checkbox" name="studySetting" bind:checked={$form.studySetting} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Study Setting
    </label>
    <label>
        <input type="checkbox" name="taskDescription" bind:checked={$form.taskDescription} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Task Description
    </label>
    <label>
        <input type="checkbox" name="taskDuration" bind:checked={$form.taskDuration} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Task Duration
    </label>
    <label>
        <input type="checkbox" name="otherStatistics" bind:checked={$form.otherStatistics} class:disabled-checkbox={$form.extractAll} disabled={$form.extractAll}>
        Other Statistics
    </label>



    <hr class="separator-quarter-length">
    <label class="toggle-label">
        Extract all of the above
        <div class="toggle">
            <input type="checkbox" name="extractAll" bind:checked={$form.extractAll}>
            <span class="slider"></span>
        </div>
    </label>
    <hr class="separator">

    <button type="button" class="btn variant-ringed-surface">Submit</button>
</form>

{#if $message}
    <p>{$message}</p>
{/if}

<SuperDebug data={$form} />