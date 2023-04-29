SELECT DATE_TRUNC('hour',cl_curr.request_timestamp) AS request_timestamp,
	cl_curr.attribute_name AS attribute_name,
	cl_curr.cluster_name AS cluster_name,
	SUM(cl_curr.cluster_count) AS curr_clusters_count,
	SUM(cl_prev.cluster_count) AS prev_clusters_count
FROM dev.clusters cl_curr
LEFT JOIN dev.clusters cl_prev ON (CAST(DATE_TRUNC('hour',cl_curr.request_timestamp) AS timestamp) + INTERVAL '-1 day') = DATE_TRUNC('hour',cl_prev.request_timestamp)
	AND cl_curr.attribute_name = cl_prev.attribute_name
	AND cl_curr.cluster_name = cl_prev.cluster_name
WHERE 1 = 1
	AND ((cl_curr.attribute_name <> 'area')
		 OR (cl_curr.attribute_name IS NULL))
	AND cl_curr.request_timestamp = (SELECT MAX(request_timestamp) FROM dev.clusters)
GROUP BY DATE_TRUNC('hour',cl_curr.request_timestamp),
	cl_curr.attribute_name,
	cl_curr.cluster_name
ORDER BY
	request_timestamp DESC,
	cl_curr.attribute_name ASC,
	curr_clusters_count DESC
