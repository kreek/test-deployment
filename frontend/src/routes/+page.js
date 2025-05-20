/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
  try {
    const response = await fetch('/data/stats.json');
    if (!response.ok) {
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
      error: 'Failed to load data'
    };
  }
}