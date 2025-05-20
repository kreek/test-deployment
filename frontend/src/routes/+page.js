import {base} from "$app/paths";

/** @type {import('./$types').PageLoad} */
export async function load({ fetch }) {
  try {
    // Add timestamp to prevent browser caching
    const timestamp = new Date().getTime();
    
    // In development, use the relative path to static/data
    // In production, the base path is already set in svelte.config.js
    const dataPath = `${base}/data/stats.json?t=${timestamp}`;
    
    console.log('Fetching data from:', dataPath);
    const response = await fetch(dataPath);
    
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