<p><label>Email: </label><input type="text" name="email" value="" required /></p>
  <p><label>Пароль: </label><input type="password" name="psw" value="" required /></p>
  <p><input type="checkbox" name="remainme"/>Не запоминать меня</p>
  <p><input type="submit" value="Войти"/></p>




{{ form.hidden_tag() }}
  <p>{{ form.email.label()}} {{ form.email() }}</p>
  <p>{{ form.psw.label()}} {{ form.psw() }}</p>
  <p>{{ form.remember.label()}} {{ form.remember() }}</p>
  <p>{{form.submit()}}</p>


{{ form.hidden_tag() }}
  <p>{{ form.email.label()}}
    {% if form.email.errors %}
      {{ form.email(class="invalid") }}
      <span class="invalid-feedback">
        {% for e in form.email.errors %}
        {{ e }}
        {% endfor %}
      </span>
    {% else %}
      {{ form.email() }}
    {% endif %}
  </p>

  <p>{{ form.psw.label()}}
    {% if form.psw.errors %}
      {{ form.psw(class="invalid") }}
      <span class="invalid-feedback">
        {% for e in form.psw.errors %}
        {{ e }}
        {% endfor %}
      </span>
    {% else %}
      {{ form.psw() }}
    {% endif %}
  </p>