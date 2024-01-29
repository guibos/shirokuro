JSON-API -> eventos de dominio
ASYNCAPI compliant

Fanout: Duplica el evento recibido por cada cola suscrita al exchange (broadcast) 📢
Direct: Permite definir una binding key a la hora de suscribir una cola al Exchange (Envía un evento a la cola si binding key de la cola == routing key del evento) 🗝
Topic: Igual que Direct, pero permitiendo el uso de wildcards en la binding key (Ej: todos los eventos que lleven el tag ‘video.*’ => …video.created, …video.description.updated, etc ) 🔑

Compañía/Empresa: Este primer nivel nos permitirá diferenciar nuestros propios eventos de los que puedan llegarnos desde terceros
Servicio: Este nivel correspondería con el Bounded Context en términos de DDD
Versión del evento: identificar la versión nos permitirá modificar el evento si fuera necesario sin que esto lleve a romper la retrocompatibilidad con los suscriptores
Tipo de mensaje: Aunque hasta ahora sólo hemos hablado de eventos, también podría darse el caso de enviar comandos asíncronos a las colas
Entidad: Este nivel correspondería con el Agregado en términos de DDD
Evento: La acción (siempre definida en pasado) que ha tenido lugar

{
  "data": {
    "id": "event id UUID",
    "type": "domain_event_name", /* codelytv.video.1.event.video.published */
    "occurred_on": "date event has occurred on", 
    "attributes": {
      "id": "aggregate id",
      "some_parameter": "some value"
    },
    "meta": {
      "some_key": "some value",
      "host": "machine hostname"
    }
  }
}

https://www.youtube.com/watch?v=AkRVD4rmTOI

<!--
title: 'AWS Simple HTTP Endpoint example in Python'
description: 'This template demonstrates how to make a simple HTTP API with Python running on AWS Lambda and API Gateway using the Serverless Framework.'
layout: Doc
framework: v3
platform: AWS
language: python
authorLink: 'https://github.com/serverless'
authorName: 'Serverless, inc.'
authorAvatar: 'https://avatars1.githubusercontent.com/u/13742415?s=200&v=4'
-->

# Serverless Framework Python HTTP API on AWS

This template demonstrates how to make a simple HTTP API with Python running on AWS Lambda and API Gateway using the Serverless Framework.

This template does not include any kind of persistence (database). For more advanced examples, check out the [serverless/examples repository](https://github.com/serverless/examples/)  which includes DynamoDB, Mongo, Fauna and other examples.

## Usage

### Deployment

```
$ serverless deploy
```

After deploying, you should see output similar to:

```bash
Deploying api_controller_aws-python-http-api-project to stage dev (us-east-1)

✔ Service deployed to stack api_controller_aws-python-http-api-project-dev (140s)

endpoint: GET - https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/
functions:
  hello: api_controller_aws-python-http-api-project-dev-hello (2.3 kB)
```

_Note_: In current form, after deployment, your API is public and can be invoked by anyone. For production deployments, you might want to configure an authorizer. For details on how to do that, refer to [http event docs](https://www.serverless.com/framework/docs/providers/aws/events/apigateway/).

### Invocation

After successful deployment, you can call the created application via HTTP:

```bash
curl https://xxxxxxx.execute-api.us-east-1.amazonaws.com/
```

Which should result in response similar to the following (removed `input` content for brevity):

```json
{
  "message": "Go Serverless v3.0! Your function executed successfully!",
  "input": {
    ...
  }
}
```

### Local development

You can invoke your function locally by using the following command:

```bash
serverless invoke local --function hello
```

Which should result in response similar to the following:

```
{
  "statusCode": 200,
  "body": "{\n  \"message\": \"Go Serverless v3.0! Your function executed successfully!\",\n  \"input\": \"\"\n}"
}
```

Alternatively, it is also possible to emulate API Gateway and Lambda locally by using `serverless-offline` plugin. In order to do that, execute the following command:

```bash
serverless plugin install -n serverless-offline
```

It will add the `serverless-offline` plugin to `devDependencies` in `package.json` file as well as will add it to `plugins` in `serverless.yml`.

After installation, you can start local emulation with:

```
serverless offline
```

To learn more about the capabilities of `serverless-offline`, please refer to its [GitHub repository](https://github.com/dherault/serverless-offline).

### Bundling dependencies

In case you would like to include 3rd party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```bash
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
