{% if '3' in cookiecutter.tests %}
import { defineConfig } from 'checkly';

export default defineConfig({
  projectName: "{{ cookiecutter.project_name }}",
  logicalId:   "{{ cookiecutter.project_slug }}",
  repoUrl:     "https://github.com/{{ cookiecutter.github_organization | default('my-org') }}/{{ cookiecutter.project_slug }}",

  checks: {
    directories: ['checkly/checks'],
    locations: ['us-east-1', 'eu-west-1']
  },

  alertSettings: {
    escalationType: 'RUN_BASED',
    runBasedEscalation: { failedRuns: 1 }
  }
});
{% endif %}
