<script setup>
import submitForm from './submitForm'
</script>

<template>
  <form @submit="submitForm" 
  action="https://questions.greatfrontend.com/api/questions/contact-form"
  method="post"
>
    <ul>
      <li>
        <label>
          Name
          <input type="text" name="name" />
        </label>
      </li>

      <li>
        <label>
          Email
          <input type="email" name="email" />
        </label>
      </li>

      <li>
        <label>
          Message
          <textarea name="message"></textarea>
        </label>
      </li>
    </ul>

    <button type="submit">Send</button>
  </form>
</template>
