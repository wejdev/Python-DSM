
/*
Users in our system can perform any of 26 different actions (represented as ‘A’ through ‘Z’),
however there was a bug where if a user performed exactly the actions A, B and C in order, their account would have a problem.
Our logs have an entry for each event that each user performs, in order, but with users mixed together into a single log.
You will write a function that takes in an array of log events and returns a list of user IDs who have the problem discussedabove
– meaning users who entered ‘A’, then ‘B’, then ‘C’ in order at some point in their history.

Log Events will be supplied in the format:

{
    userId: "bob",
    eventChar: "A",
    timestamp:  (DateTime of the Event)
}

Implement the ‘DoWork’ method in the supplied code, which is passed a list of the above objects.
Return an List containing each userId which has the ‘ABC’ problem described above.
While this test code has been setup with a single, relatively easy example input (which does contain a broken user id),
your code should be designed to be as performant as possible and to work with any data set which matches the rules laid out above.


using System;
using System.Collections.Generic;

class Solution
{
    class LogItem
    {
        public string userId;
        public char eventChar;
        public DateTime timestamp;

        public static LogItem New(string user, char evt) => new LogItem() { userId = user, eventChar = evt, timestamp = DateTime.Now };
    }

    static List<string> DoWork(List<LogItem> items)
    {
        //IMPLEMENT HERE
        throw new NotImplementedException("Implement here");
    }

    static void Main(string[] args)
    {
        var items = new List<LogItem>();
        items.Add(LogItem.New("bob", 'V'));
        items.Add(LogItem.New("bob", 'A'));
        items.Add(LogItem.New("steve", 'A'));
        items.Add(LogItem.New("bob", 'B'));
        items.Add(LogItem.New("bob", 'C'));
        items.Add(LogItem.New("bob", 'C'));
        items.Add(LogItem.New("steve", 'B'));
        items.Add(LogItem.New("sally", 'B'));
        items.Add(LogItem.New("steve", 'C'));
        items.Add(LogItem.New("sally", 'C'));
        items.Add(LogItem.New("sally", 'A'));

        var check = DoWork(items);

        if (check.Count != 2)
            throw new Exception("Wrong number of items");
        if (!check.Contains("bob"))
            throw new Exception("Missing 'bob'");
        if (!check.Contains("steve"))
            throw new Exception("Missing 'steve'");

        Console.WriteLine("Tests passed");
    }
}

 */

using System;
using System.Collections.Generic;
using System.Linq;

class Solution
{
	class LogItem
	{
		public string userId = string.Empty;
		public char eventChar;
		public DateTime timestamp;

		public static LogItem New(string user, char evt) =>
			new LogItem() { userId = user, eventChar = evt, timestamp = DateTime.Now };
	}

	static List<string> DoWork(List<LogItem> items)
	{
		const string badSequence = "ABC";
		var eventsByUserDict = new Dictionary<string, string>();

		foreach (var li in items)
		{
			eventsByUserDict.TryGetValue(li.userId, out string? curEvents);
			eventsByUserDict[li.userId] = (curEvents ?? string.Empty) + li.eventChar;
		};

		return eventsByUserDict
				.Where(kvp => kvp.Value.Contains(badSequence))
				.Select(kvp => kvp.Key)
				.ToList();
	}

	static void Main(string[] args)
	{
		var items = new List<LogItem>();
		items.Add(LogItem.New("bob", 'V'));
		items.Add(LogItem.New("bob", 'A'));
		items.Add(LogItem.New("steve", 'A'));
		items.Add(LogItem.New("bob", 'B'));
		items.Add(LogItem.New("bob", 'C'));
		items.Add(LogItem.New("bob", 'C'));
		items.Add(LogItem.New("steve", 'B'));
		items.Add(LogItem.New("sally", 'B'));
		items.Add(LogItem.New("steve", 'C'));
		items.Add(LogItem.New("sally", 'C'));
		items.Add(LogItem.New("sally", 'A'));

		var check = DoWork(items);

		if (check.Count != 2)
			throw new Exception("Wrong number of items");
		if (!check.Contains("bob"))
			throw new Exception("Missing 'bob'");
		if (!check.Contains("steve"))
			throw new Exception("Missing 'steve'");

		Console.WriteLine("Tests passed");
	}
}
