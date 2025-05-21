
# Synchronous-and-Asynchronous-Programming
Description and example code of Synchronous and Asynchronous Programming
<br>
<h1>Synchronous Programming</h1>
<p>Done Sequentially and in a specific order.Program's flow is always from top to bottom</p>
<p>Synchronous programming, on the other hand, is advantageous for developers. Synchronous programming is much easier to code. It’s well supported among all programming languages, and as the default programming method</p>
<h3>When to use? </h3>
<p>Suitable where tasks have dependencies or require sequential processing or operations are quick and don't involve long waiting tasks e.g: command-line tools, basic data processing scripts.</p>

<h3>Pros</h3>
<ul>
  <li>Simplicity</li>
  <li>Ease if debugging</li>
  <li>Predictability</li>
</ul>
<h3>Cons</h3>
<ul>
  <li>Inefficient with I/O bound tasks</li>
</ul>

<h1>Asynchronous Programming</h1>
<p>Done Parallely.Asynchronous tasks can run concurrently, utilizing resources more efficiently.</p>
<h3>When to use?</h3>
<p>Suitable when getting data from external sources(databases, API) or real-time processing e.g: chat applications, streaming services.</p>
<p>Asynchronous programming allows more things to be done simultaneously and is typically used to enhance the user experience by providing an effortless, quick-loading flow.</p>
<p>Example: A web server can handle 1000 requests at the same time without getting blocked.
</p>
<h3>Pros</h3>
<ul>
  <li>Concurrency</li>
  <li>Responsiveness</li>
  <li>Scalability</li>
</ul>
<h3>Cons</h3>
<ul>
  <li>Complexity</li>
</ul>
