<script>
  /** @type {import('./$types').PageData} */
  export let data;
  
  $: ({ stats, error } = data);
</script>

<h1>Dashboard</h1>

{#if error}
  <p class="error">{error}</p>
{:else if stats}
  <div class="stats">
    <p>Last Updated: {new Date(stats.last_updated).toLocaleString()}</p>
    
    <h2>Stats</h2>
    <ul>
      <li>Users: {stats.stats.users}</li>
      <li>Events: {stats.stats.events}</li>
      <li>Avg Response Time: {stats.stats.average_response_time}s</li>
    </ul>
    
    <h2>Recent Events</h2>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Event</th>
          <th>Timestamp</th>
        </tr>
      </thead>
      <tbody>
        {#each stats.events as event}
          <tr>
            <td>{event.id}</td>
            <td>{event.name}</td>
            <td>{new Date(event.timestamp).toLocaleString()}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
{:else}
  <p>Loading...</p>
{/if}

<style>
  .error {
    color: red;
    font-weight: bold;
  }
  
  .stats {
    max-width: 800px;
    margin: 0 auto;
  }
  
  table {
    width: 100%;
    border-collapse: collapse;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  th {
    background-color: #f2f2f2;
  }
</style>