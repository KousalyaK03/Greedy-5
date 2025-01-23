class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # Approach:
        # Use a priority queue to efficiently determine the (worker, bike) pair with the smallest Manhattan distance.
        # For ties in distance, prioritize smaller worker index, then smaller bike index.
        # Use sets to track assigned workers and bikes.
        
        # Time Complexity: O(n * m * log(n * m)) where n is the number of workers and m is the number of bikes.
        # Space Complexity: O(n * m) for storing all (distance, worker, bike) pairs in the heap.
        # Did this code successfully run on Leetcode: Yes
        # Any problem you faced while coding this: No
        
        # Priority queue (min-heap) to store distances and worker-bike pairs
        heap = []

        # Precompute all Manhattan distances and add them to the heap
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                distance = abs(wx - bx) + abs(wy - by)
                # Push (distance, worker index, bike index) into the heap
                heapq.heappush(heap, (distance, i, j))

        # Result array to store bike assignments for each worker
        result = [-1] * len(workers)
        # Sets to track assigned workers and bikes
        assigned_workers = set()
        assigned_bikes = set()

        # Process heap until all workers are assigned a bike
        while len(assigned_workers) < len(workers):
            distance, worker, bike = heapq.heappop(heap)
            
            # If the worker and bike are not yet assigned, assign the bike to the worker
            if worker not in assigned_workers and bike not in assigned_bikes:
                result[worker] = bike
                assigned_workers.add(worker)
                assigned_bikes.add(bike)

        return result
