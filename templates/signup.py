<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>sign up</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='signup.css') }}">
    <link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css"rel="stylesheet">
</head>

<body>
    
<div >
  <div class="main-div" >
    <div class="secend-div">
      <div class="sm:mx-auto sm:w-full sm:max-w-sm">
        <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900" style="padding-bottom: 20px;">Sign up to your account</h2>
      </div>

      <div>
        <form class="space-y-6" action="/signup" method="POST">
          <div>
            <label for="username" class="block text-sm font-medium leading-6 text-gray-900">Username</label>
            <div class="mt-2">
              <input id="username" name="username" type="username" autocomplete="username" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" style="line-height: 2rem;">
            </div>
          </div>

          <div>
            <div class="flex items-center justify-between">
              <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
              <div class="text-sm">
              </div>
            </div>
            <div class="mt-2">
              <input id="password" name="password" type="password" autocomplete="current-password" required class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" style="line-height: 2rem;">
            </div>
          </div>

          <div class="button-signup">
            <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Submet</button>
          </div>
        </form>

        <p class="mt-10 text-center text-sm text-gray-500">
          Have account?
          <a href="{{url_for('signin')}}" class="font-semibold leading-6 text-indigo-600 hover:text-indigo-500">Sign In</a>
        </p>
      </div>
    </div>
  </div>


</body>
</html>
