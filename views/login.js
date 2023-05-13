function login (doc) {
    if (doc && doc.username && doc.password ){
      emit(doc.username, {password: doc.password});
    }
  }