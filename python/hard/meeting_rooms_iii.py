# https://leetcode.com/problems/meeting-rooms-iii/description/?envType=daily-question&envId=2024-02-18
# quite hard to wrap my head around this one. nice problem


# first attempt -- had to use the LC hints, but didn't reference any solutions fortunately
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])

        # room #
        rooms = [i for i in range(n)]
        heapq.heapify(rooms)
        # counter for times room has been used
        count = [0] * n
        # ongoing meetings
        ongoing = []
        heapq.heapify(ongoing)

        for meeting in meetings:
            start, end = meeting[0], meeting[1]

            # update ongoing meetings that have ended
            while len(ongoing) > 0 and ongoing[0][0] <= start:
                finished = heapq.heappop(ongoing)
                heapq.heappush(rooms, finished[1])

            # get room for this meeting [end_time,room#]
            if len(rooms) > 0:
                # look in rooms first for openings
                room = heapq.heappop(rooms)
                ongoing_meeting = [end, room]
                heapq.heappush(ongoing, ongoing_meeting)
                count[room] += 1
            else:
                # use room from soonest-ending ongoing mtg if no room is available
                ongoing_end, room = heapq.heappop(ongoing)
                # update end time of this meeting based on the ongoing mtg in its room
                delay = ongoing_end - start
                end += delay
                delayed_meeting = [end, room]
                heapq.heappush(ongoing, delayed_meeting)
                count[room] += 1

        # check count to find most mtgs in a room
        most = room = 0
        for i, c in enumerate(count):
            if c > most:
                most = c
                room = i
        return room


# cleaned up my first solution a bit--beats 62% time and 61% memory
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        rooms = [i for i in range(n)]
        ongoing = []
        heapq.heapify(rooms)
        heapq.heapify(ongoing)

        count = [0] * n
        for meeting in meetings:
            start, end = meeting[0], meeting[1]

            while len(ongoing) > 0 and ongoing[0][0] <= start:
                _, room = heapq.heappop(ongoing)
                heapq.heappush(rooms, room)

            if len(rooms) > 0:
                room = heapq.heappop(rooms)
                meeting = [end, room]
            else:
                ongoing_end, room = heapq.heappop(ongoing)
                delay = ongoing_end - start
                meeting = [end + delay, room]

            heapq.heappush(ongoing, meeting)
            count[room] += 1

        most = room = 0
        for i, c in enumerate(count):
            if c > most:
                room, most = i, c
        return room
