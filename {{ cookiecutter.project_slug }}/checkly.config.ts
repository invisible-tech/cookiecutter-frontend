{% if cookiecutter.tests_flags.e2e %}
import 'dotenv/config'
import { defineConfig } from 'checkly'
import { Frequency } from 'checkly/constructs'

/*
  These default Checkly settings should work for most projects.
  Feel free to tweak the settings to fit your team’s objectives.
*/

export default defineConfig({
  projectName: "{{ cookiecutter.project_name }}",   // shown in the Checkly dashboard
  logicalId:   "{{ cookiecutter.project_slug }}",  // unique ID for your checks
  repoUrl:     "https://github.com/invisible-tech/{{ cookiecutter.project_slug }}",

  checks: {
    activated: true,   // turn all checks on or off
    muted:     false,  // silence alerts when you’re doing maintenance
    runtimeId: '2025.04',
    frequency: Frequency.EVERY_10M,    // API checks every 10 minutes
    locations: ['us-east-1', 'eu-west-1'],

    checkMatch: '**/src/checks/**/*.check.ts',  // pick up your API-style checks

    browserChecks: {
      frequency: Frequency.EVERY_30M,           // UI/E2E checks every 30 minutes
      testMatch: '**/src/checks/**/*.spec.ts' 
    }
  },

  cli: {
    runLocation: 'us-east-1' 
  },

  alertSettings: {
    escalationType: 'RUN_BASED',
    runBasedEscalation: { failedRuns: 1 }  // alert on first failure
  }
})
{% endif %}
