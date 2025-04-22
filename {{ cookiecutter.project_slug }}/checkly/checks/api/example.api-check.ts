{% if '3' in cookiecutter.tests %}
import { ApiCheck, group } from 'checkly/constructs';
import { getAuthToken } from '../../helpers/auth.js';

if (!process.env.CHECKLY_BASE_URL) {
  throw new Error("Missing CHECKLY_BASE_URL environment variable.");
}

group('Smoke API', () => {
  new ApiCheck('health-endpoint', {
    name: 'GET /health',
    method: 'GET',
    url: `${process.env.CHECKLY_BASE_URL}/health`,
    assertions: [
      { type: 'STATUS_CODE', comparison: 'EQUALS', target: 200 }
    ]
  });

  new ApiCheck('users-list', {
    name: 'GET /users',
    method: 'GET',
    url: `${process.env.CHECKLY_BASE_URL}/users`,
    setupScript: async (ctx) => {
      ctx.request.headers['Authorization'] = `Bearer ${await getAuthToken()}`;
    },
    assertions: [
      { type: 'STATUS_CODE', comparison: 'EQUALS', target: 200 },
      { type: 'JSON_BODY', property: 'length', comparison: 'GREATER_THAN', target: 0 }
    ]
  });
});
{% endif %}
