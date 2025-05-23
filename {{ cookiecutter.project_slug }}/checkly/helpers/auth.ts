{% if cookiecutter.tests_flags.e2e %}
export async function getAuthToken() {
  const res = await fetch(process.env.AUTH_URL as string, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      clientId: process.env.CLIENT_ID,
      clientSecret: process.env.CLIENT_SECRET
    })
  });

  if (!res.ok) {
    const errorText = await res.text();
    throw new Error(`Auth failed: ${res.status} ${res.statusText}. Response: ${errorText}`);
  }

  const { access_token } = await res.json();
  return access_token as string;
}
{% endif %}
