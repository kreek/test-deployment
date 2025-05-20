/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
  try {
    // Add timestamp to prevent browser caching
    const timestamp = new Date().getTime();
    const response = await fetch(`/data/stats.json?t=${timestamp}`);
    if (!response.ok) {
      console.error(`Failed to load data: ${response.status} ${response.statusText}`);
      return {
        stats: null,
        error: `Failed to load data: ${response.status} ${response.statusText}`
      };
    }
    const stats = await response.json();
    return { stats };
  } catch (error) {
    console.error('Error loading stats:', error);
    return {
      stats: null,
      error: 'Failed to load data: ' + (error.message || String(error))
    };
  }
}