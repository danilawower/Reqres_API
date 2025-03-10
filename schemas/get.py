single_user_schema = {
  "type": "object",
  "properties": {
      "data": {"type": "object", "properties": {"id": {"type": "integer"},
      "email": {"type": "string"},
      "first_name": {"type": "string"},
      "last_name": {"type": "string"},
      "avatar": {"type": "string"}
      },
      "required": ["id", "email", "first_name", "last_name", "avatar"]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "data",
    "support"
  ]
}

single_user_not_found_schema = {}

list_user_schema = {
  "type": "object",
  "properties": {
    "page": {
      "type": "number"
    },
    "per_page": {
      "type": "number"
    },
    "total": {
      "type": "number"
    },
    "total_pages": {
      "type": "number"
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "email": {
            "type": "string"
          },
          "first_name": {
            "type": "string"
          },
          "last_name": {
            "type": "string"
          },
          "avatar": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "email",
          "first_name",
          "last_name",
          "avatar"
        ]
      }
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "page",
    "per_page",
    "total",
    "total_pages",
    "data",
    "support"
  ]
}


list_schema = {
  "type": "object",
  "properties": {
    "page": {
      "type": "number"
    },
    "per_page": {
      "type": "number"
    },
    "total": {
      "type": "number"
    },
    "total_pages": {
      "type": "number"
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "name": {
            "type": "string"
          },
          "year": {
            "type": "number"
          },
          "color": {
            "type": "string"
          },
          "pantone_value": {
            "type": "string"
          }
        },
        "required": [
          "id",
          "name",
          "year",
          "color",
          "pantone_value"
        ]
      }
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    }
  },
  "required": [
    "page",
    "per_page",
    "total",
    "total_pages",
    "data",
    "support"
  ]
}