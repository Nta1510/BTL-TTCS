{% extends "base.html" %}
{% block content %}
  <h2>Sent Messages</h2>
  <ul>
    {% for msg in messages %}
      <li>
        <strong>{{ msg.subject }}</strong> to {{ msg.recipient.username }} at {{ msg.timestamp }}
      </li>
    {% empty %}
      <li>No sent messages.</li>
    {% endfor %}
  </ul>
{% endblock %}

